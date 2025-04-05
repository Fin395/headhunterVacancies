import json
import os
from typing import Optional

from config import DEFAULT_JSON
from src.base_file import BaseFile
from src.utils import from_vacancy_to_dict
from src.vacancy import Vacancy


class FileManager(BaseFile):
    """Класс для работы с файлами, наследуемый от базового класса BaseFile"""

    def __init__(self, name: Optional[str] = DEFAULT_JSON) -> None:
        """Метод инициализации экземпляра класса для работы с файлами"""
        self.__name = name
        self.check_and_create()

    def check_and_create(self) -> None:
        """Проверяем, существует ли файл с вакансиями, и если нет - создаем файл с пустым списком"""
        if not os.path.exists(self.__name):
            with open(self.__name, "w", encoding="utf-8") as file:
                file.write("[]")

    @property
    def name(self) -> str:
        """Создаем геттер для получения значения приватного атрибута '__name'"""
        return self.__name

    def add_to_file(self, new_vacancies: list[Vacancy]) -> None:
        """Сохраняем отобранные по критериям пользователя вакансии в файл с проверкой на наличие дубликатов"""
        new_vacancies_as_dict = from_vacancy_to_dict(new_vacancies)

        with open(self.__name, "r", encoding="utf-8") as f:
            vacancies = json.load(f)

            if len(vacancies) == 0:
                vacancies.extend(new_vacancies_as_dict)
            else:
                vacancies_list_id = [vacancy["id"] for vacancy in vacancies]
                for new_vacancy in new_vacancies_as_dict:
                    if new_vacancy["id"] not in vacancies_list_id:
                        vacancies.append(new_vacancy)

        with open(self.__name, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, indent=4, ensure_ascii=False)

    def get_from_file(self) -> None:
        """Получаем из файла список сохраненных вакансий"""
        with open(self.__name, "r", encoding="utf-8") as f:
            vacancies = json.load(f)
        for vacancy in vacancies:
            print(vacancy)

    def remove_from_file(self) -> None:
        """Удаляем вакансии из файла и оставляем пустой список"""
        with open(self.__name, "w", encoding="utf-8") as file:
            file.write("[]")
