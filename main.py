# -*- coding: utf-8 -*-
import sys

from src.letterboxd_classes import LetterBoxdDiaryStatistics
from src.letterboxd_utils import create_numeric_info, create_table

arguments = sys.argv[1:]


def main():
    data_file = arguments[0]
    selected_year = arguments[1]

    statistics = LetterBoxdDiaryStatistics(data_file, selected_year)

    create_numeric_info("Total Movies", statistics.count_movies())
    create_numeric_info("Total Rewatches", statistics.count_rewatches())
    create_numeric_info("Ratings Average", statistics.avg_ratings())
    create_table("Movies By Ratings", "rating,movies", statistics.movies_by_rating())
    create_table("Movies By Tags", "tags,movies", statistics.movies_by_tag())
    create_table("Movies By Year", "year,movies", statistics.movies_by_year())
    create_table("Lazy Reviews", "days in review,movies", statistics.lazy_reviews())
    create_table("Reviews by Month", "month,reviews", statistics.reviews_by_month())
    create_table("Watches by Month", "month,watches", statistics.watches_by_month())


if __name__ == "__main__":
    main()
