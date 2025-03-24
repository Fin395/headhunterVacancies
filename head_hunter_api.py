from src.base_api import BaseApi
import requests


class HeadHunterAPI(BaseApi):
    """Создаем на основе базового класса BaseApi класс для работы с API"""
    def __init__(self):
        """Метод подключения к API"""
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__()

    def connect_api(self):
        response = requests.get(self.url, headers=self.headers, params=self.params)
        print(response.status_code)

