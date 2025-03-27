from typing import Optional

from src.base_file import BaseFile


class FileManager(BaseFile):
    """Класс для работы с файлами, наследуемый от базового класса BaseFile"""

    def __init__(self, name: Optional[str] = "json_file.json") -> None:
        self.__name = name

    def add_to_file(self, vacancies):
        with open(self.__name, "w", encoding="utf-8") as file:
            for vacancy in vacancies:
                file.write(f"{vacancy}\n")

