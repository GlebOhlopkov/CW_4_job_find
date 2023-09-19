from class_api import SuperJobAPI
from class_vacancies import Vacancy
import json

# создание экземпляра для работы с API сайта superjob.ru
sj_api = SuperJobAPI()

# получение вакансий связанных с Python
sj_vacancies = sj_api.get_vacancies()

# сохранение всех полученных вакансий в файл для дальнейшей обработки пользователем
sj_api.save_to_file(sj_vacancies)


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
