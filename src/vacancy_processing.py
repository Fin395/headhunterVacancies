from typing import Any


class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("id", "name", "url", "salary", "currency", "requirement")

    def __init__(self, id, name: str, url: str, salary: dict, requirement: dict) -> None:
        """Определяем атрибуты класса и применяем методы их валидации при инициализации"""
        self.id = id
        self.name = name
        self.url = url
        self.salary = salary
        self.__validate_salary(salary)
        self.requirement = requirement
        self.__validate_requirement(requirement)

    def __str__(self) -> str:
        """Магический метод преобразования экземпляра класса в строку"""
        return f'id вакансии: {self.id}, наименование вакансии: {self.name}, ссылка на вакансию: {self.url}, зарплата: {self.salary}, требования: {self.requirement}'

    def __lt__(self, other: "Vacancy") -> bool:
        """Магический метод, позволяющий сравнивать значения зарплат между собой"""
        return self.salary < other.salary


    def __gt__(self, other: "Vacancy") -> bool:
        """Магический метод, позволяющий сравнивать значения зарплат между собой"""
        return self.salary > other.salary


    @classmethod
    def from_dict(cls, vacancies: list[dict]) -> list:
        """Класс-метод, определяющий значения атрибутов объекта класса исходя
        из полученных по API данных с сайта hh.ru и преобразующий указанные данные
         в список экземпляров класса Vacancy"""
        vacancy_obj_list = []
        for vacancy in vacancies:
            id, name, url, salary, requirement = (
                vacancy["id"],
                vacancy["name"],
                vacancy["alternate_url"],
                vacancy["salary"],
                vacancy["snippet"]["requirement"],
            )
            vacancy_obj_list.append(cls(id, name, url, salary, requirement))
        return vacancy_obj_list

    def __validate_salary(self, salary: None | dict) -> int:
        if salary is None:
            self.salary = 0
        elif isinstance(salary, dict):
            if not salary["from"] is None and not salary["to"] is None:
                self.salary = salary["to"]
            elif not salary["from"] is None and salary["to"] is None:
                self.salary = salary["from"]
            else:
                self.salary = salary["to"]
        return self.salary

    def __validate_requirement(self, requirement: None | dict) -> str:
        if requirement is None:
            self.requirement = "Не указано"
        return self.requirement
