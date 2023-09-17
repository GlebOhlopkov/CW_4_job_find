
class Vacancy():
    def __init__(self, dict_from_api):
        self.name = dict_from_api['objects'][0]['profession']
        self.url = dict_from_api['objects'][0]['client']['link']
        self.salary = [dict_from_api['objects'][0]['payment_from'], dict_from_api['objects'][0]['payment_to']]
        self.info = dict_from_api['objects'][0]['candidat']
        self.published_time = dict_from_api['objects'][0]['date_published']
        self.town = dict_from_api['objects'][0]['town']['tittle']
