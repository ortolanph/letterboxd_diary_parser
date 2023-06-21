import csv
import datetime

from src.letterboxd_aggregators import same_rating, contains_tag, same_year, same_review_time, same_review_month, \
    same_watched_month
from src.letterboxd_utils import parse_date, parse_tags, is_rewatch, calculate_review_time, identity_transformer, \
    to_month_transformer, to_sinple_movie


class LetterBoxdDiary:
    date = datetime.date.today()
    name = ""
    year = 0
    uri = ""
    rating = 0.0
    rewatch = False
    tags = []
    watched_date = datetime.date.today()

    def to_string(self):
        return f"""Date..........: {self.date}
Name..........: {self.name}
Year..........: {self.year}
URI...........: {self.uri}
Rating........: {self.rating}
Rewatch.......: {self.rewatch}
Tags..........: {self.tags}
Watched Date..: {self.watched_date}"""


class LetterBoxdDiaryStatistics:
    data_file = ""
    __diary_entries = []
    __ratings_set = set()
    __tags_set = set()
    __years_set = set()
    __review_times = set()
    __review_months = set()
    __watches_months = set()

    __genre_dict = dict()
    __source_dict = dict()
    __adaptation_dict = dict()

    def __init__(self, data_file_name, year):
        self.data_file = data_file_name
        self.__read_csv(year)

    def __read_csv(self, year):
        with open(self.data_file) as data:
            csv_reader = csv.DictReader(data, delimiter=',')

            for row in csv_reader:
                watched_year = parse_date(row["Watched Date"]).year

                if int(year) == watched_year:
                    my_diary_entry = LetterBoxdDiary()
                    my_diary_entry.date = parse_date(row["Date"])
                    my_diary_entry.name = row["Name"]
                    my_diary_entry.year = int(row["Year"])
                    my_diary_entry.uri = row["Letterboxd URI"]
                    my_diary_entry.rating = float(row["Rating"])
                    my_diary_entry.tags = parse_tags(row["Tags"])
                    my_diary_entry.rewatch = is_rewatch(row["Rewatch"])
                    my_diary_entry.watched_date = parse_date(row["Watched Date"])

                    self.__ratings_set.add(my_diary_entry.rating)
                    self.__tags_set.update(my_diary_entry.tags)
                    self.__years_set.add(my_diary_entry.year)
                    self.__review_times.add(calculate_review_time(my_diary_entry.date, my_diary_entry.watched_date))
                    self.__review_months.add(my_diary_entry.date.month)
                    self.__watches_months.add(my_diary_entry.watched_date.month)

                    self.__diary_entries.append(my_diary_entry)

                    self.__populate_genre_dict(my_diary_entry.tags)
                    self.__populate_source_dict(my_diary_entry.tags)
                    self.__populate_based_on_dict(my_diary_entry.tags)

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

    def __populate_based_on_dict(self, tags):
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

    def movies_by_rating(self):
        return self.__get_data(self.__ratings_set, same_rating, identity_transformer)

    def movies_by_year(self):
        return self.__get_data(self.__years_set, same_year, identity_transformer)

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

        return map(to_sinple_movie, sorted_movies)

    def genres(self):
        return self.__genre_dict

    def sources(self):
        return self.__source_dict

    def adaptations(self):
        return self.__adaptation_dict
