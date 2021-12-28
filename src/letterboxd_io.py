import os
import shutil

from src.letterboxd_constants import TARGET_PATH, SOURCE_PATH, STYLE_FILE


def __has_target_folder():
    return os.path.exists(TARGET_PATH)


def prepare_target_folder():
    if __has_target_folder():
        shutil.rmtree(TARGET_PATH)

    os.mkdir(TARGET_PATH)
    shutil.copyfile(f"{SOURCE_PATH}{os.sep}{STYLE_FILE}",
                    f"{TARGET_PATH}{os.sep}{STYLE_FILE}")
