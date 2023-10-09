import yaml

from src.letterboxd_constants import CONFIG_FILE


class ConfigManager:
    _config_data = dict()

    def __init__(self):
        print("Loading configurations")
        with open(CONFIG_FILE) as config_file:
            self._config_data = yaml.safe_load(config_file)

        print(self._config_data)

    def get_tmdb_config(self):
        return self._config_data["tmdb"]
