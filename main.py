# -*- coding: utf-8 -*-
import sys

from src.letterboxd_classes import LetterBoxdDiaryStatistics
from src.letterboxd_constants import GRAPH_DICT, TEMPLATE_GRAPH_DATA
from src.letterboxd_graphs import generate_pie_graph
from src.letterboxd_io import prepare_target_folder
from src.letterboxd_reporter import create_report
from src.letterboxd_utils import format_duration

arguments = sys.argv[1:]


def main():
    data_file = arguments[0]
    selected_year = arguments[1]

    statistics = LetterBoxdDiaryStatistics(data_file, selected_year)

    GRAPH_DICT["WATCHES_MONTH"]["data"] = list(statistics.watches_by_month().values())
    GRAPH_DICT["WATCHES_MONTH"]["labels"] = list(statistics.watches_by_month().keys())

    sorted_genres = dict(sorted(statistics.genres().items(), key=lambda item: item[1]))
    GRAPH_DICT["WATCHED_GENRES"]["data"] = list(sorted_genres.values())
    GRAPH_DICT["WATCHED_GENRES"]["labels"] = list(sorted_genres.keys())

    sorted_sources = dict(sorted(statistics.sources().items(), key=lambda item: item[1]))
    GRAPH_DICT["WATCHED_SOURCES"]["data"] = list(sorted_sources.values())
    GRAPH_DICT["WATCHED_SOURCES"]["labels"] = list(sorted_sources.keys())

    sorted_adaptations = dict(sorted(statistics.adaptations().items(), key=lambda item: item[1]))
    GRAPH_DICT["WATCHED_ADAPTATIONS"]["data"] = list(sorted_adaptations.values())
    GRAPH_DICT["WATCHED_ADAPTATIONS"]["labels"] = list(sorted_adaptations.keys())

    time_data = {
        "total_time": format_duration(statistics.total_time()),
        "average_time": format_duration(statistics.avg_time()),
        "longest_movie_name": statistics.longest_movie()["movie"],
        "longest_movie_runtime": format_duration(statistics.longest_movie()["runtime"]),
        "shortest_movie_name": statistics.shortest_movie()["movie"],
        "shortest_movie_runtime": format_duration(statistics.shortest_movie()["runtime"]),
    }

    prepare_target_folder()

    create_report(
        selected_year,
        statistics.count_movies(),
        statistics.count_rewatches(),
        statistics.avg_ratings(),
        statistics.create_movie_table(),
        time_data,
        TEMPLATE_GRAPH_DATA)

    for graph in GRAPH_DICT:
        generate_pie_graph(GRAPH_DICT[graph])


if __name__ == "__main__":
    main()
