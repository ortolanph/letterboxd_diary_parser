import os

from jinja2 import Template

from src.letterboxd_constants import TARGET_PATH, SOURCE_PATH, TEMPLATE_FILE, TARGET_FILE


def create_report(year, watched, rewatches, average, movies, time_data, graph_data):
    with open(os.path.join(SOURCE_PATH, TEMPLATE_FILE)) as file_:
        template = Template(file_.read())

    rendered_report = template.render(
        year=year,
        watched=watched,
        rewatches=rewatches,
        average=average,
        movies=movies,
        total_time=time_data["total_time"],
        average_time=time_data["average_time"],
        longest_movie_name=time_data["longest_movie_name"],
        longest_movie_runtime=time_data["longest_movie_runtime"],
        shortest_movie_name=time_data["shortest_movie_name"],
        shortest_movie_runtime=time_data["shortest_movie_runtime"],
        graphs=graph_data)

    with open(os.path.join(TARGET_PATH, TARGET_FILE), 'a') as writer:
        writer.writelines(rendered_report)

    file_.close()
    writer.close()
