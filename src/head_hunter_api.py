from src.base_api import BaseApi
import requests

from src.exception import InputException


class HeadHunter(BaseApi):
    """Создаем на основе базового класса BaseApi класс для работы с HH"""

    __url: str
    __headers: dict
    __params: dict
    __vacancies: list


    def __init__(self) -> None:
        """Метод инициализации экземпляра класса"""
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100, 'area': 113}
        self.__vacancies = []
        super().__init__()

    def _BaseApi__connect_api(self) -> None:
        """Метод для проверки подключения к API"""
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        if response.status_code != 200: # проверяем статус кода-ответа
            raise requests.exceptions.RequestException

    def get_vacancies(self, keyword: str) -> list:
        """Метод получения данных о вакансиях с сайта hh.ru """
        if len(keyword) == 0:
            raise InputException("Введите ключевое слово.")
        self.__params['text'] = keyword
        try:
            self._BaseApi__connect_api()
            while self.__params.get('page') != 20:
                response = requests.get(self.__url, headers=self.__headers, params=self.__params)
                vacancies = response.json()['items']
                self.__vacancies.extend(vacancies)
                self.__params['page'] += 1
        except requests.exceptions.RequestException as e:
            print(f"Не удалось получить данные. Возникла ошибка: {e}")
            return []
        else:
            if len(self.__vacancies) == 0:
                raise InputException("По Вашему запросу вакансий не найдено")
            else:
                return self.__vacancies
