from abc import ABC, abstractmethod
from typing import Any


class BaseApi(ABC):
    """Абстрактный класс для работы с API"""
    pass

    @abstractmethod
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Абстрактный метод для инициализации экземпляра класса"""
        pass

    @abstractmethod
    def connect_api(self, *args: Any, **kwargs: Any) -> None:
        """Абстрактный метод подключения к API"""
        pass

    # @abstractmethod
    # def get_vacancies(self, *args: Any, **kwargs: Any) -> None:
    #     """Абстрактный метод для получения вакансий"""
    #     pass
