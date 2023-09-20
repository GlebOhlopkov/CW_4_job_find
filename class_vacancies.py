class Vacancy:
    """
    Класс для создания вакансии
    """

    def __init__(self, vacancy_dict: dict):
        """
        Создание экземпляра класса вакансии
        :param vacancy_dict: словарь с данными по профессии
        """
        self.name = vacancy_dict['name']
        self.url = vacancy_dict['url']
        self.salary_from = vacancy_dict['salary_from']
        self.salary_to = vacancy_dict['salary_to']
        self.info = vacancy_dict['info']
        self.published_time = vacancy_dict['published_time']
        self.town = vacancy_dict['town']

    def _str__(self):
        return f'''Вакансия - {self.name},
Сводная информация - {self.info}
Зарплата - {self.salary_from} - {self.salary_to}
Город - {self.town}
Дата публикации - {self.published_time}
Ссылка - {self.url}
'''

    def __le__(self, other: int):
        """
        Метод для сравнения зарплаты вакансии
        :param other: требуемое значение зарплаты
        :return: True, если наивысшее из значений зарплаты вакансии меньше требуемой
        """
        return max(self.salary_from, self.salary_to) <= other

    def __ge__(self, other: int):
        """
        Метод для сравнения зарплаты вакансии
        :param other: требуемое значение зарплаты
        :return: True, если наивысшее из значений зарплаты вакансии больше требуемой
        """
        return max(self.salary_from, self.salary_to) >= other

    @classmethod
    def create_vacancy_from_hh(cls, vac_dic_hh):
        """Метод для создания экземпляра класса Vacancy из словаря сайта headhunter.ru"""
        vacancy_info = {
            'name': vac_dic_hh['name'],
            'url': vac_dic_hh['alternate_url'],
            'salary_from': vac_dic_hh['salary']['from'],
            'salary_to': vac_dic_hh['salary']['to'],
            'info': vac_dic_hh['snippet']['requirement'],
            'published_time': vac_dic_hh['published_at'],
            'town': vac_dic_hh['area']['name'],
        }
        return Vacancy(vacancy_info)

    @classmethod
    def create_vacancy_from_sj(cls, vac_dic_sj):
        """Метод для создания экземпляра класса Vacancy из словаря сайта superjob.ru"""
        vacancy_info = {
            'name': vac_dic_sj['profession'],
            'url': vac_dic_sj['link'],
            'salary_from': vac_dic_sj['payment_from'],
            'salary_to': vac_dic_sj['payment_to'],
            'info': vac_dic_sj['candidat'],
            'published_time': vac_dic_sj['date_published'],
            'town': vac_dic_sj['town']['title'],
        }
        return Vacancy(vacancy_info)
