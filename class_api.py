import requests
from abc import ABC, abstractmethod
import os


class BaseAPI(ABC):
    """
    Абстрактный класс для работы с API
    """

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(BaseAPI):
    """
    Класс для работы с API сайта www.headhunter.ru
    """

    def __init__(self):
        """
        Создание экземпляра класса сайта https://api.hh.ru/vacancies
        """
        self.url_address = 'https://api.hh.ru/vacancies'

    def get_vacancies(self) -> dict:
        """
        Функция для получения данных сайта

        :return данные в формате словаря
        """
        response = requests.get(self.url_address, params={'per_page': 100, 'area': 1, 'text': 'Python', 'period': 7})
        vacancies_dict = response.json()
        return vacancies_dict['items']


class SuperJobAPI(BaseAPI):
    """
    Класс для работы с API сайта www.superjob.ru
    """

    SJ_API_KEY = os.getenv('SuperJob_API_KEY')

    def __init__(self):
        """
        Создание экземпляра класса сайта https://api.superjob.ru/2.0/vacancies/
        """
        self.url_address = 'https://api.superjob.ru/2.0/vacancies/'

    def get_vacancies(self) -> dict:
        """
        Функция для получения данных сайта

        :return данные в формате словаря
        """
        response = requests.get(self.url_address,
                                headers={'X-Api-App-Id': self.SJ_API_KEY},
                                params={'count': 100, 'town': 'Москва', 'keywords': 'Python', 'period': 7})
        vacancies_dict = response.json()
        return vacancies_dict['objects']
