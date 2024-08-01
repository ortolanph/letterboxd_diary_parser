import csv

from src.config_manager import ConfigManager
from src.letterboxd_utils import format_duration
from src.tmdb_integration import TMDBIntegration


def get_episodes_duration_sum(episodes):
    all_runtimes = list(int(episode['runtime']) for episode in episodes)
    return sum(all_runtimes)


def get_shows_ratings(shows):
    all_ratings = dict()

    for show in shows:
        all_ratings[show['name']] = show['rating']

    return all_ratings


def main(year):
    configuration = ConfigManager()
    tmdb_client = TMDBIntegration(configuration.get_tmdb_config())

    csv_file = f"shows_{year}.csv"
    total_shows_duration_sum = 0

    with open(csv_file) as show_data:
        show_reader = csv.DictReader(show_data)

        for show_row in show_reader:
            show_data = tmdb_client.get_show_data(show_row["TMDB_ID"], int(show_row["Season"]))

            episodes_sum = get_episodes_duration_sum(show_data['episodes'])
            print(
                f"{show_row['TV_Show']} "
                f"Season {show_row['Season']} "
                f"on {show_row['Source']} has a total time of {format_duration(episodes_sum)}")

            total_shows_duration_sum += episodes_sum

    print(f"All the shows watched on {year} has a total of {format_duration(total_shows_duration_sum)}")

    page = 2

    ratings_response = tmdb_client.tv_show_ratings()
    all_show_ratings = get_shows_ratings(ratings_response["results"])

    total_pages = int(ratings_response["total_pages"])

    while page <= total_pages:
        ratings_response = tmdb_client.tv_show_ratings(page)
        all_show_ratings.update(get_shows_ratings(ratings_response[ratings_response["results"]]))
        page += 1

    print(all_show_ratings)


if __name__ == '__main__':
    main(2024)
