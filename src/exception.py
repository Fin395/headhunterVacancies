from typing import Any


class InputException(Exception):
    """Создаем пользовательский класс исключения для обработки введенных пользователем данных"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Инициализация экземпляра класса"""
        if args:
            self.message = args[0]
        else:
            self.message = "По указанным критериям данные отсутствуют."

    def __str__(self) -> str:
        """Магический метод, который возвращает текст ошибки"""
        return self.message
