import inspect

from src.exception import InputException
from src.vacancy import Vacancy


def filter_by_words(vacancies: list, keywords: list) -> list:
    """Вспомогательная функция, которая фильтрует список вакансий по введенным пользователем ключевым словам"""
    if len(keywords) == 0:
        raise InputException("Введите слова для поиска.")
    else:
        for word in keywords:
            vacancies_filtered_by_words = list(filter(lambda x: word in x.requirement.lower(), vacancies))
            if len(vacancies_filtered_by_words) == 0:
                raise InputException("Вакансий с таким описанием не найдено")
            return vacancies_filtered_by_words



def filter_by_salary(vacancies_list: list, salary_range: str) -> list | None:
    """Вспомогательная функция, которая фильтрует список вакансий по диапазону зарплаты, полученного от пользователя"""
    if len(salary_range) == 0:
        raise InputException("Введите значения: 'от' и 'до'")
    else:
        split_salary_range = salary_range.split("-")
        if len(split_salary_range) == 1 and split_salary_range[0].isdigit():
            salary_range_from = int(split_salary_range[0])
            salary_range_to = salary_range_from
        elif len(split_salary_range) == 2 and [word.isdigit() for word in split_salary_range]:
            salary_range_from = int(salary_range.split("-")[0])
            salary_range_to = int(salary_range.split("-")[1])
        else:
            raise InputException("Неверный формат ввода. Введите данные в формате 'от'-'до'")

        if salary_range_from > salary_range_to:
            raise InputException("Значение 'от' не может быть больше значения 'до'")
        elif all(vacancy.salary < salary_range_from or vacancy.salary > salary_range_to for vacancy in vacancies_list):
            raise InputException("Вакансий с такой зарплатой не найдено. Попробуйте поискать что-нибудь другое.")
        elif any(salary_range_to >= vacancy.salary >= salary_range_from for vacancy in vacancies_list):
            vacancies_filtered_by_salary = list(
                filter(lambda x: salary_range_to >= x.salary >= salary_range_from, vacancies_list)
            )
            return vacancies_filtered_by_salary


def sort_vacancies(list_vacancies_objects: list) -> list:
    """Вспомогательная функция, которая сортирует вакансии по зарплате от большего к меньшему"""
    sorted_vacancies = sorted(list_vacancies_objects, reverse=True)
    return sorted_vacancies


def get_top_vacancies(vacancies: list, number: int) -> list:
    """Получаем топ-N вакансий с наивысшей зарплатой (N получаем от пользователя)"""
    return vacancies[0:number]


def from_vacancy_to_dict(vacancies: list[Vacancy]) -> list[dict]:
    """Преобразуем список экземпляров класса Vacancy в список словарей,
    в которых ключи соответствуют атрибутам экземпляра"""
    vacancies_dict_list = []
    for vacancy in vacancies:
        dict_from_vacancy = {
            attr: val
            for attr, val in inspect.getmembers(vacancy)
            if not attr.startswith("__") and not inspect.ismethod(val)
        }
        vacancies_dict_list.append(dict_from_vacancy)
    return vacancies_dict_list
