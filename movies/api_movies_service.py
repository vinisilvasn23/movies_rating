import requests
from django.conf import settings


class ApiMoviesService:
    def __init__(self):
        self.base_url = settings.API_BASE_URL
        self.api_key = settings.MOVIE_API_KEY
        self.bearer_token = settings.MOVIE_API_TOKEN

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.bearer_token}",
            "Content-Type": "application/json",
        }

    def listMoviesPopular(self, page):
        url = f"{self.base_url}movie/popular"
        params = {"api_key": self.api_key, "page": page}
        response = requests.get(url, params=params, headers=self._get_headers())
        return response

    def listBestRated(self, page):
        url = f"{self.base_url}movie/top_rated"
        params = {"api_key": self.api_key, "page": page}
        response = requests.get(url, params=params, headers=self._get_headers())
        return response

    def listMoviesMovieTheater(self, page):
        url = f"{self.base_url}movie/now_playing"
        params = {"api_key": self.api_key, "page": page, "region": "BR"}
        response = requests.get(url, params=params, headers=self._get_headers())
        return response

    def filterMovies(self, query):
        url = f"{self.base_url}search/movie"
        params = {"api_key": self.api_key, "language": "pt-BR", "query": query}
        response = requests.get(url, params=params, headers=self._get_headers())
        return response

    def getMovieById(self, id_movie):
        url = f"{self.base_url}movie/{id_movie}"
        params = {"api_key": self.api_key, "language": "pt-BR"}
        response = requests.get(url, params=params, headers=self._get_headers())
        return response

    def getCreditsMovie(self, id_movie):
        url = f"{self.base_url}movie/{id_movie}/credits"
        params = {"api_key": self.api_key, "language": "pt-BR"}
        response = requests.get(url, params=params, headers=self._get_headers())
        return response

    def getProviders(self, id_movie):
        url = f"{self.base_url}movie/{id_movie}/watch/providers"
        params = {"api_key": self.api_key}
        response = requests.get(url, params=params, headers=self._get_headers())
        return response

    def getGenres(self):
        url = f"{self.base_url}genre/movie/list"
        params = {"api_key": self.api_key, "language": "pt-BR"}
        response = requests.get(url, params=params, headers=self._get_headers())
        return response

    def discoverMovies(self, page):
        url = f"{self.base_url}discover/movie"
        params = {
            "api_key": self.api_key,
            "include_adult": False,
            "sort_by": "vote_count.desc",
            "page": page,
        }
        response = requests.get(url, params=params, headers=self._get_headers())
        return response

    def createSession(self, token):
        url = f"{self.base_url}authentication/session/new"
        params = {"api_key": self.api_key}
        response = requests.post(url, json=token, headers=self._get_headers())
        return response

    def translation(self, id_movie):
        url = f"{self.base_url}movie/{id_movie}/translations"
        params = {"api_key": self.api_key}
        response = requests.get(url, params=params, headers=self._get_headers())
        return response

    def listSeriesPopular(self, page):
        url = f"{self.base_url}tv/popular"
        params = {"api_key": self.api_key, "page": page}
        response = requests.get(url, params=params, headers=self._get_headers())
        return response

    def topSeries(self, page):
        url = f"{self.base_url}tv/top_rated"
        params = {"api_key": self.api_key, "page": page}
        response = requests.get(url, params=params, headers=self._get_headers())
        return response
