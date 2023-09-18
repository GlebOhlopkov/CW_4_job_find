import requests
import json
from abc import ABC, abstractmethod
from class_to_file import SaveToJSONFile
import os


class BaseAPI(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(BaseAPI, SaveToJSONFile):

    def __init__(self):
        self.url_address = 'https://api.hh.ru/vacancies'
        SaveToJSONFile.__init__(self)

    def get_vacancies(self):
        response = requests.get(self.url_address)  # headers={'HH-User-Agent': 'MyApp/1.0 (my-app-feedback@example.com)'})
        vacancies_dict = json.loads(response.text)
        return vacancies_dict


class SuperJobAPI(BaseAPI, SaveToJSONFile):
    SJ_API_KEY = os.getenv('SuperJob_API_KEY')

    def __init__(self):
        self.url_address = 'https://api.superjob.ru/2.0/vacancies/'
        SaveToJSONFile.__init__(self)

    def get_vacancies(self):
        response = requests.get(self.url_address,
                                headers={'X-Api-App-Id': self.SJ_API_KEY},
                                params={'count': 100, 'town': 'Москва', 'keywords': 'Python'})
        vacancies_dict = json.loads(response.text)
        return vacancies_dict['objects']
