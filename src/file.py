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
            json.dump(vacancies, file, indent=4, ensure_ascii=False)

    # def get_from_file(self):
    #     with open(self.__name, "r", encoding="utf-8") as f:
    #         vacancies = f.read()
    #     print(vacancies)
