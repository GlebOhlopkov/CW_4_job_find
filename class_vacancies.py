class Vacancy():
    def __init__(self, vac_dict):
        self.name = vac_dict['profession']
        self.url = vac_dict['client']['link']
        self.salary = vac_dict['payment_from'], vac_dict['payment_to']
        self.info = vac_dict['candidat']
        self.published_time = vac_dict['date_published']
        self.town = vac_dict['town']['tittle']

    @classmethod
    def create_vacancy_from_dict(cls, vac_dict):
        for vac in vac_dict:
            cls(vac)
