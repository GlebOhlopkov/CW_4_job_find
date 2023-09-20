from class_api import SuperJobAPI, HeadHunterAPI
from class_vacancies import Vacancy
from class_to_file import SaveToJSONFile
import json


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

# файл для сохранения отфильтрованных вакансий с сайта headhunter.ru
hh_choice = 'hh_choice_vacancy.json'
# файл для сохранения отфильтрованных вакансий с сайта superjob.ru
sj_choice = 'sj_choice_vacancy.json'
# создание экземпляра для сохранения отфильтрованных вакансий hh.ru в файл
hh_save_choice_vac = SaveToJSONFile(hh_choice)
# создание экземпляра для сохранения отфильтрованных вакансий sj.ru в файл
sj_save_choice_vac = SaveToJSONFile(sj_choice)


def user_interaction():
    """
    Функция для работы с пользователем
    :return:
    """

    # Запрос у пользователя необходимых критериев
    need_salary = int(input("Введите требуемую зарплату: "))

    # Обработка полученных вакансий сайта headhunter.ru с требованиями пользователя
    data_hh = hh_save_all_vac.load_file()
    # Новый словарь для обработанных вакансий
    new_vac_dict_hh = {'vacancy': []}
    for vac in data_hh:
        if type(vac['salary']) == dict:
            new_vac = Vacancy.create_vacancy_from_hh(vac)
            # Проверка требований пользователя
            if new_vac.check_salary(need_salary):
                new_vac_dict_hh['vacancy'].append(vac)
            else:
                continue
    # Запись отфильтрованных вакансий в отдельный файл
    hh_save_choice_vac.save_to_file(new_vac_dict_hh)

    # Обработка полученных вакансий сайта superjob.ru с требованиями пользователя
    data_sj = sj_save_all_vac.load_file()
    # Новый словарь для обработанных вакансий
    new_vac_dict_sj = {'vacancy': []}
    for vac in data_sj:
        new_vac = Vacancy.create_vacancy_from_sj(vac)
        # Проверка требований пользователя
        if new_vac.check_salary(need_salary):
            new_vac_dict_sj['vacancy'].append(vac)
        else:
            continue
    # Запись отфильтрованных вакансий в отдельный файл
    sj_save_choice_vac.save_to_file(new_vac_dict_sj)

    print('Возможны следующие предложения:')
    print('--- HeadHunter.ru ---')
    # Вывод обработанных вакансий сайта headhunter.ru
    choice_hh = hh_save_choice_vac.load_file()
    for count, vac in enumerate(choice_hh['vacancy']):
        new_vac = Vacancy.create_vacancy_from_hh(vac)
        print(f'---> Вакансия №{count+1}\n{new_vac}')
    print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n')

    print('--- SuperJob.ru: ---')
    # Вывод обработанных вакансий сайта superjob.ru
    choice_sj = sj_save_choice_vac.load_file()
    for count,vac in enumerate(choice_sj['vacancy']):
        new_vac = Vacancy.create_vacancy_from_sj(vac)
        print(f'---> Вакансия №{count+1}\n{new_vac}')


if __name__ == "__main__":
    user_interaction()
