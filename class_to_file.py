import json
from abc import ABC, abstractmethod


class SaveToFile(ABC):
    """
    Абстрактный класс для сохранения данных в файл
    """

    @abstractmethod
    def save_to_file(self, data_dict):
        pass


class SaveToJSONFile(SaveToFile):
    """
    Класс для сохранения данных в json-файл
    """

    def save_to_file(self, data_dict: dict) -> None:
        """
        Функция сохраняет выбранный словарь в json-файл

        :param data_dict: словарь с данными в формате json
        :return: запись данных в файл 'all_vacancies.json'
        """
        with open('all_vacancies.json', 'w', encoding='utf-8') as json_file:
            return json.dump(data_dict, json_file, indent=4)
