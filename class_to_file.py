from abc import ABC, abstractmethod


class SaveLoadToFile(ABC):

    @abstractmethod
    def save_to_file(self, data_dict):
        pass


class SaveToJSONFile(SaveLoadToFile):

    def save_to_file(self, data_dict):
        with open('all_vacancies.json', 'w', encoding='utf-8') as json_file:
            return json_file.write(data_dict)
