from abc import ABC, abstractmethod
from typing import Any


class FileManager(ABC):
    """Базовый класс для работы с файлами"""
    pass

    @abstractmethod
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Абстрактный метод для инициализации экземпляра класса"""
        pass

    @abstractmethod
    def add_to_file(self, *args: Any, **kwargs: Any) -> None:
        """Абстрактный метод для записи данных в файл"""
        pass

    @abstractmethod
    def get_from_file(self, *args: Any, **kwargs: Any) -> None:
        """Абстрактный метод для получения данных из файла"""
        pass

    @abstractmethod
    def remove_from_file(self, *args: Any, **kwargs: Any) -> None:
        """Абстрактный метод для удаления данных из файла класса"""
        pass
