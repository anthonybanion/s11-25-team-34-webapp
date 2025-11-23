#Contiene funciones para interactuar con la API de Climatiq
import requests
class ClimatiqClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.climatiq.io/v1/"

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    def get_emission_factors(self, params=None):
        url = self.base_url + "emission-factors"
        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()
    def calculate_emissions(self, data):
        url = self.base_url + "calculate"
        response = requests.post(url, headers=self._get_headers(), json=data)
        response.raise_for_status()
        return response.json()
    def get_activities(self, params=None):
        url = self.base_url + "activities"
        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()
    def get_sources(self, params=None):
        url = self.base_url + "sources"
        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()
    def get_categories(self, params=None):
        url = self.base_url + "categories"
        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()
    def get_units(self, params=None):
        url = self.base_url + "units"
        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()
    def get_geographies(self, params=None):
        url = self.base_url + "geographies"
        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()
    def get_data_quality(self, params=None):
        url = self.base_url + "data-quality"
        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()
    def get_metadata(self, params=None):
        url = self.base_url + "metadata"
        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()
    def get_version(self):
        url = self.base_url + "version"
        response = requests.get(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json()
    