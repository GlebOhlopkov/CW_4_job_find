import requests
import json
from abc import ABC, abstractmethod
import os


class BaseAPI(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(BaseAPI):

    def __init__(self):
        self.url_address = 'https://api.hh.ru/vacancies'

    def get_vacancies(self):
        vacancies_dict = requests.get(self.url_address)  # headers={'HH-User-Agent': 'MyApp/1.0 (my-app-feedback@example.com)'})
        return vacancies_dict.json()


class SuperJobAPI(BaseAPI):
    SJ_API_KEY = os.getenv('SuperJob_API_KEY')

    def __init__(self):
        self.url_address = 'https://api.superjob.ru/2.0/vacancies/'

    def get_vacancies(self):
        vacancies_dict = requests.get(self.url_address, headers={'X-Api-App-Id': self.SJ_API_KEY}, params={'count': 100})
        return vacancies_dict.json()
