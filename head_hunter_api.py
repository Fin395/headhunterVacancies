from src.base_api import BaseApi
import requests


class HeadHunter(BaseApi):
    """Создаем на основе базового класса BaseApi класс для работы с HH"""

    __url: str
    __headers: dict
    __params: dict
    __vacancies: list


    def __init__(self):
        """Метод инициализации экземпляра класса"""
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []
        super().__init__()

    def __connect_api(self):
        """Метод подключения к API"""
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        if response.status_code != 200:
            raise requests.exceptions.RequestException



# hh = HeadHunterAPI()
# hh.connect_api()