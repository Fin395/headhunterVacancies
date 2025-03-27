import json
from typing import Optional

from config import DEFAULT_JSON
from src.base_file import BaseFile


class FileManager(BaseFile):
    """Класс для работы с файлами, наследуемый от базового класса BaseFile"""

    def __init__(self, name: Optional[str] = DEFAULT_JSON) -> None:
        self.__name = name

    def add_to_file(self, vacancies):
        with open(self.__name, "a", encoding="utf-8") as file:
            for vacancy in vacancies:
                file.write(f"{vacancy}\n")
