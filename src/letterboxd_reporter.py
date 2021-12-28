import os

from jinja2 import Template

from src.letterboxd_constants import TARGET_PATH, SOURCE_PATH, TEMPLATE_FILE, TARGET_FILE


def create_report(watched, rewatches, average, movies):
    with open(os.path.join(SOURCE_PATH, TEMPLATE_FILE)) as file_:
        template = Template(file_.read())

    rendered_report = template.render(
        watched=watched,
        rewatches=rewatches,
        average=average,
        movies=movies)

    with open(os.path.join(TARGET_PATH, TARGET_FILE), 'a') as writer:
        writer.writelines(rendered_report)

    file_.close()
    writer.close()
