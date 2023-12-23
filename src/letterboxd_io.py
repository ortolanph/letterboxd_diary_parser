import os
import shutil

from src.letterboxd_constants import TARGET_PATH, SOURCE_PATH


def __has_target_folder():
    return os.path.exists(TARGET_PATH)


def prepare_target_folder():
    if __has_target_folder():
        shutil.rmtree(TARGET_PATH)

    # os.mkdir(TARGET_PATH)
    shutil.copytree(f"{SOURCE_PATH}{os.sep}",
                    f"{TARGET_PATH}{os.sep}")
