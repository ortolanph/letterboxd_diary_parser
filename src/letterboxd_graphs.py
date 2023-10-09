import os

import matplotlib.pyplot as plotter
import numpy

from src.letterboxd_constants import TARGET_PATH


def generate_graph(statistics, graph_opts):
    y_pos = numpy.arange(len(statistics["labels"]))

    plotter.rcParams['figure.figsize'] = [graph_opts["width"], graph_opts["height"]]
    plotter.bar(y_pos, statistics["data"])
    plotter.xticks(y_pos, statistics["labels"], rotation=45)
    plotter.title(graph_opts["title"])
    plotter.ylabel(graph_opts["ylabel"])
    plotter.xlabel(graph_opts["xlabel"])

    plotter.savefig(fname=f"{TARGET_PATH}{os.sep}{graph_opts['filename']}",
                    format="png")

    plotter.clf()
    plotter.cla()
    plotter.close()


def generate_pie_graph(graph_dict):
    plotter.rcParams['figure.figsize'] = [8, 8]

    plotter.pie(
        graph_dict["data"],
        labels=graph_dict["labels"],
        autopct=lambda x: '{:.0f}'.format(x * sum(graph_dict["data"]) / 100)
    )

    plotter.title(graph_dict["title"])

    plotter.savefig(fname=f"{TARGET_PATH}{os.sep}{graph_dict['filename']}",
                    format="png")

    plotter.clf()
    plotter.cla()
    plotter.close()
