from class_to_file import SaveToJSONFile
import json


class Vacancy(SaveToJSONFile):
    """
    Класс для создания вакансии
    """

    def __init__(self, vac_dict: dict):
        """
        Создание экземпляра класса вакансии
        :param vac_dict: словарь с данными по профессии
        """
        self.name = vac_dict['profession']
        self.url = vac_dict['client']['link']
        self.salary = vac_dict['payment_from'], vac_dict['payment_to']
        self.info = vac_dict['candidat']
        self.published_time = vac_dict['date_published']
        self.town = vac_dict['town']['title']
        SaveToJSONFile.__init__(self)

    def save_to_file(self, data_dict: dict) -> None:
        """
        Функция сохраняет выбранный словарь в json-файл

        :param data_dict: словарь с данными в формате json
        :return: запись данных в файл 'choice_vacancies.json'
        """
        with open('choice_vacancies.json', 'a', encoding='utf-8') as json_file:
            return json.dump(data_dict, json_file, indent=4)

    @classmethod
    def create_vacancy_from_dict(cls, vac_dict):
        for vac in vac_dict:
            cls(vac)
