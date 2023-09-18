import json
from abc import ABC, abstractmethod


class SaveToFile(ABC):

    @abstractmethod
    def save_to_file(self, data_dict):
        pass


class SaveToJSONFile(SaveToFile):

    def save_to_file(self, data_dict):
        with open('all_vacancies.json', 'w', encoding='utf-8') as json_file:
            return json.dump(data_dict, json_file)
