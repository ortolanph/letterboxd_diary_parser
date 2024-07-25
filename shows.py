import csv
import json

from src.config_manager import ConfigManager
from src.letterboxd_utils import format_duration
from src.tmdb_integration import TMDBIntegration

CSV_FILE = "shows_2024.csv"

def get_episodes_duration_sum(episodes):
    all_runtimes = list(int(episode['runtime']) for episode in episodes)
    return sum(all_runtimes)

def main():
    configuration = ConfigManager()
    tmdb_client = TMDBIntegration(configuration.get_tmdb_config())

    with open(CSV_FILE) as show_data:
        show_reader = csv.DictReader(show_data)
        total_shows_duration_sum = 0

        for show_row in show_reader:
            show_data = tmdb_client.get_show_data(show_row["TMDB_ID"], int(show_row["Season"]))

            with open(f'{show_row["TMDB_ID"]}.json', 'w') as show_file:
                show_file.writelines(json.dumps(show_data))
                show_file.close()

            episodes_sum = get_episodes_duration_sum(show_data['episodes'])
            print(f"{show_row['TV_Show']} Season {show_row['Season']} on {show_row['Source']} has a total time of {format_duration(episodes_sum)}")

            total_shows_duration_sum += episodes_sum

        print(f"All the shows watched on 2023 has a total of {format_duration(total_shows_duration_sum)}")


if __name__ == '__main__':
    main()
