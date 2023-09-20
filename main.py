from class_api import SuperJobAPI, HeadHunterAPI
from class_vacancies import Vacancy
from class_to_file import SaveToJSONFile
import json

# создание экземпляра для работы с API сайта superjob.ru
sj_api = SuperJobAPI()
# файл для сохранения вакансий с сайта superjob.ru
sj_json_path = 'sj_all_vacancies.json'
# создание экземпляра для сохранения вакансий sj.ru в файл
sj_save_all_vac = SaveToJSONFile(sj_json_path)
# получение вакансий связанных с Python
sj_vacancies = sj_api.get_vacancies()
# сохранение всех вакансий sj.ru в файл
sj_save_all_vac.save_to_file(sj_vacancies)

# создание экземпляра для работы с API сайта headhunter.ru
hh_api = HeadHunterAPI()
# файл для сохранения вакансий с сайта headhunter.ru
hh_json_path = 'hh_all_vacancies.json'
# создание экземпляра для сохранения вакансий hh.ru в файл
hh_save_all_vac = SaveToJSONFile(hh_json_path)
# получение вакансий связанных с Python
hh_vacancies = hh_api.get_vacancies()
# сохранение всех вакансий hh.ru в файл
hh_save_all_vac.save_to_file(hh_vacancies)


def user_interaction():
    """
    Функция для работы с пользователем
    :return:
    """

    # Запрос у пользователя необходимых критериев
    need_salary = int(input("Введите требуемую зарплату: "))

    # Обработка полученных вакансий с требованиями пользователя
    with open('all_vacancies.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        # Новый словарь для обработанных вакансий
        new_vac_dict = {'vacancy': []}
        for vac in data:
            new_vac = Vacancy(vac)
            # Проверка требований пользователя
            if min(new_vac.salary) >= need_salary:
                new_vac_dict['vacancy'].append(vac)
            else:
                continue
        # Запись отфильтрованных вакансий в отдельный файл
        with open('choice_vacancies.json', 'a', encoding='utf-8') as new_file:
            json.dump(new_vac_dict, new_file, indent=4)

    print('Возможны следующие предложения:')

    # Вывод обработанных вакансий
    with open('choice_vacancies.json', 'r', encoding='utf-8') as new_file:
        data = json.load(new_file)
        for vac in data['vacancy']:
            new_vac = Vacancy(vac)
            print(new_vac.name)
            print(new_vac.salary)
            print(new_vac.info)
            print('___')


if __name__ == "__main__":
    user_interaction()
