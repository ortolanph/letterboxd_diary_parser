import json

import requests

BASE_URL = "https://api.themoviedb.org/3/"


class TMDBIntegration:
    _configuration = dict()

    def __init__(self, tmdb_configuration):
        self._configuration = tmdb_configuration

    def authenticate(self):
        url = "authentication"
        return self._execute_url(url)

    def find_movie_by_id(self, movie_id):
        url = f"movie/{movie_id}"
        parameters = {"language": "en-US"}
        return self._execute_url(url, parameters)

    def get_show_data(self, show_id, season):
        url = f"tv/{show_id}/season/{season}"
        parameters = {"language": "en-US"}
        return self._execute_url(url, parameters)

    def _execute_url(self, url, parameters=None):
        if parameters is None:
            parameters = {}
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self._configuration['header']}"
        }

        request_url = self._configuration['base_url'] + url

        return json.loads(requests.get(request_url, headers=headers, params=parameters).text)
