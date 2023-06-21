# -*- coding: utf-8 -*-
import sys

from src.letterboxd_graphs import generate_graph
from src.letterboxd_classes import LetterBoxdDiaryStatistics
from src.letterboxd_constants import GRAPH_DICT, TEMPLATE_GRAPH_DATA
from src.letterboxd_io import prepare_target_folder
from src.letterboxd_reporter import create_report
from src.letterboxd_utils import create_graph_data

arguments = sys.argv[1:]


def main():
    data_file = arguments[0]
    selected_year = arguments[1]

    statistics = LetterBoxdDiaryStatistics(data_file, selected_year)

    GRAPH_DICT["RATINGS"]["data"]["statistics"] = \
        create_graph_data(statistics.movies_by_rating(),
                          GRAPH_DICT["RATINGS"]["data"]["sort"])

    GRAPH_DICT["WATCHES_MONTH"]["data"]["statistics"] = \
        create_graph_data(statistics.watches_by_month(),
                          GRAPH_DICT["WATCHES_MONTH"]["data"]["sort"])

    GRAPH_DICT["WATCHED_GENRES"]["data"]["statistics"] = \
        create_graph_data(statistics.genres(),
                          GRAPH_DICT["WATCHED_GENRES"]["data"]["sort"])

    GRAPH_DICT["WATCHED_SOURCES"]["data"]["statistics"] = \
        create_graph_data(statistics.sources(),
                          GRAPH_DICT["WATCHED_SOURCES"]["data"]["sort"])

    GRAPH_DICT["WATCHED_ADAPTATIONS"]["data"]["statistics"] = \
        create_graph_data(statistics.adaptations(),
                          GRAPH_DICT["WATCHED_ADAPTATIONS"]["data"]["sort"])

    prepare_target_folder()

    create_report(
        selected_year,
        statistics.count_movies(),
        statistics.count_rewatches(),
        statistics.avg_ratings(),
        statistics.create_movie_table(),
        TEMPLATE_GRAPH_DATA)

    for graph in GRAPH_DICT:
        generate_graph(
            GRAPH_DICT[graph]["data"]["statistics"],
            GRAPH_DICT[graph]["graph"])


if __name__ == "__main__":
    # files = os.listdir("src")
    # print(files)
    main()
