import csv
import datetime

from src.config_manager import ConfigManager
from src.letterboxd_aggregators import same_watched_month
from src.letterboxd_utils import parse_date, parse_tags, is_rewatch, to_month_transformer, to_simple_movie, collect_tags
from src.tmdb_integration import TMDBIntegration


class LetterBoxdDiary:
    date = datetime.date.today()
    name = ""
    year = 0
    uri = ""
    rating = 0.0
    rewatch = False
    tags = []
    watched_date = datetime.date.today()
    imdb_id = ""
    tmdb_id = 0
    runtime = 0
    poster_path = ""  # https://image.tmdb.org/t/p/original/{{poster_path}}

    def to_string(self):
        return f"""
Date..........: {self.date}
Name..........: {self.name}
Year..........: {self.year}
URI...........: {self.uri}
Rating........: {self.rating}
Rewatch.......: {self.rewatch}
Tags..........: {self.tags}
Watched Date..: {self.watched_date}
IMDB ID.......: {self.imdb_id}
TMDB ID.......: {self.tmdb_id}
Runtime.......: {self.runtime}
Poster Path...: {self.poster_path}
"""


class LetterBoxdDiaryStatistics:
    data_file = ""
    __diary_entries = []
    __tags_set = set()
    __review_times = set()
    __review_months = set()
    __watches_months = set()

    __genre_dict = dict()
    __source_dict = dict()
    __adaptation_dict = dict()
    __animation_dict = dict()

    __tmdb_integration = None

    __total_time = 0
    __longest_movie = dict()
    __longest_movie_runtime = 0
    __shortest_movie = dict()
    __shortest_movie_runtime = 9999999
    __avg_time = 0.0
    __total_movies_with_runtime = 0

    def __init__(self, data_file_name, year):
        self.data_file = data_file_name

        config_manager = ConfigManager()
        self.__tmdb_integration = TMDBIntegration(config_manager.get_tmdb_config())
        self.__tmdb_integration.authenticate()

        self.__read_csv(year)

    def __read_csv(self, year):
        with open(self.data_file) as data:
            csv_reader = csv.DictReader(data, delimiter=',')

            for row in csv_reader:
                print(f'Movie: {row["Name"]}')
                watched_year = parse_date(row["Watched Date"]).year

                if int(year) == watched_year:
                    print(" - Getting information from data source")
                    my_diary_entry = LetterBoxdDiary()
                    my_diary_entry.date = parse_date(row["Date"])
                    my_diary_entry.name = row["Name"]
                    my_diary_entry.year = int(row["Year"])
                    my_diary_entry.uri = row["Letterboxd URI"]
                    my_diary_entry.rating = float(row["Rating"])
                    my_diary_entry.tags = parse_tags(row["Tags"])
                    my_diary_entry.rewatch = is_rewatch(row["Rewatch"])
                    my_diary_entry.watched_date = parse_date(row["Watched Date"])

                    collected_tags = collect_tags(my_diary_entry.tags)

                    if row["TMDB ID"] != "":
                        my_diary_entry.tmdb_id = int(row["TMDB ID"])
                    else:
                        my_diary_entry.tmdb_id = int(collected_tags["tmdb_id"])

                    print(" - Fetching other data on TMDB")
                    if my_diary_entry.tmdb_id > -1:
                        movie = self.__tmdb_integration.find_movie_by_id(my_diary_entry.tmdb_id)
                        runtime = int(movie['runtime'])
                        my_diary_entry.runtime = runtime
                        self.__total_time += runtime

                        my_diary_entry.imdb_id = movie['imdb_id']
                        my_diary_entry.poster_path = movie['poster_path']

                        if runtime < self.__shortest_movie_runtime:
                            self.__shortest_movie = {'movie': my_diary_entry.name, 'runtime': runtime}
                            self.__shortest_movie_runtime = runtime

                        if runtime > self.__longest_movie_runtime:
                            self.__longest_movie = {'movie': my_diary_entry.name, 'runtime': runtime}
                            self.__longest_movie_runtime = runtime

                        self.__total_movies_with_runtime += 1

                    print(" - Separating data")
                    self.__tags_set.update(my_diary_entry.tags)
                    self.__review_months.add(my_diary_entry.date.month)
                    self.__watches_months.add(my_diary_entry.watched_date.month)

                    self.__diary_entries.append(my_diary_entry)

                    self.__populate_genre_dict(my_diary_entry.tags)
                    self.__populate_source_dict(my_diary_entry.tags)
                    self.__populate_adaptation_dict(my_diary_entry.tags)
                    self.__populate_animations_dict(my_diary_entry.tags)

        print("Done")

    def __populate_genre_dict(self, tags):
        genre_tags = [tag.split(":")[1] for tag in tags if tag.strip().startswith("genre:")]

        for genre_tag in genre_tags:
            if genre_tag in self.__genre_dict:
                self.__genre_dict[genre_tag] += 1
            else:
                self.__genre_dict[genre_tag] = 1

    def __populate_source_dict(self, tags):
        source_tags = [tag.split(":")[1] for tag in tags if tag.strip().startswith("source:")]

        for source_tag in source_tags:
            if source_tag in self.__source_dict:
                self.__source_dict[source_tag] += 1
            else:
                self.__source_dict[source_tag] = 1

    def __populate_adaptation_dict(self, tags):
        based_on_tags = [tag.split(":")[1].strip() for tag in tags if tag.strip().startswith("adaptation:")]

        for based_on_tag in based_on_tags:
            if based_on_tag in self.__adaptation_dict:
                self.__adaptation_dict[based_on_tag] += 1
            else:
                self.__adaptation_dict[based_on_tag] = 1

    def __get_data(self, data_set, aggregator, transformer):
        result_dict = {}
        for data_key in data_set:
            movies = map(
                lambda e: e.name, filter(lambda entry: aggregator(entry, data_key), self.__diary_entries))
            result_dict[transformer(data_key)] = len(list(movies))

        return result_dict

    def __populate_animations_dict(self, tags):
        if "style:animation" in tags:
            self.__animation_dict["Animation"] = self.__animation_dict.get("Animation", 0) + 1
        else:
            self.__animation_dict["Live Action"] = self.__animation_dict.get("Live Action", 0) + 1

    def total_time(self):
        return self.__total_time

    def avg_time(self):
        return self.total_time() / self.__total_movies_with_runtime

    def longest_movie(self):
        return self.__longest_movie

    def shortest_movie(self):
        return self.__shortest_movie

    def watches_by_month(self):
        return self.__get_data(self.__watches_months, same_watched_month, to_month_transformer)

    def count_rewatches(self):
        movies = filter(lambda e: e.rewatch, self.__diary_entries)
        return len(list(movies))

    def count_movies(self):
        return len(self.__diary_entries)

    def sum_ratings(self):
        all_ratings = list(map(lambda e: e.rating, self.__diary_entries))
        return sum(all_ratings)

    def avg_ratings(self):
        return round(self.sum_ratings() / self.count_movies(), 2)

    def create_movie_table(self):
        sorted_movies = self.__diary_entries
        sorted_movies.sort(key=lambda e: e.watched_date)

        return map(to_simple_movie, sorted_movies)

    def genres(self):
        return self.__genre_dict

    def sources(self):
        return self.__source_dict

    def adaptations(self):
        return self.__adaptation_dict

    def animations(self):
        return self.__animation_dict
