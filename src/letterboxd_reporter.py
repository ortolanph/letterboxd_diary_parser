import os
import shutil

from jinja2 import Template

__SOURCE_PATH = "templates"
__TARGET_PATH = "target"
__TEMPLATE_FILE = "letterboxd.template"
__TARGET_FILE = "letterboxd.html"
__STYLE_FILE = "letterboxd.css"


def __has_target_folder():
    return os.path.exists(__TARGET_PATH)


def __prepare_target_folder():
    if __has_target_folder():
        shutil.rmtree(__TARGET_PATH)

    os.mkdir(__TARGET_PATH)
    shutil.copyfile(f"{__SOURCE_PATH}{os.sep}{__STYLE_FILE}",
                    f"{__TARGET_PATH}{os.sep}{__STYLE_FILE}")


def create_report(watched, rewatches, average, movies):
    __prepare_target_folder()

    with open(os.path.join(__SOURCE_PATH, __TEMPLATE_FILE)) as file_:
        template = Template(file_.read())

    rendered_report = template.render(
        watched=watched,
        rewatches=rewatches,
        average=average,
        movies=movies)

    with open(os.path.join(__TARGET_PATH, __TARGET_FILE), 'a') as writer:
        writer.writelines(rendered_report)

    file_.close()
    writer.close()
