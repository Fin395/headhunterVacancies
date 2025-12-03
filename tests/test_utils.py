import pytest

from src.exception import InputException
from src.utils import filter_by_salary, filter_by_words, get_top_vacancies, sort_vacancies
from src.vacancy import Vacancy


def test_filter_by_words(vacancies_obj_list: list[Vacancy], keywords_for_filter: list[str]) -> None:
    """Проверяем корректность фильтрации по заданным словам"""
    filtered_vacancies = filter_by_words(vacancies_obj_list, keywords_for_filter)
    assert len(filtered_vacancies) == 2
    assert filtered_vacancies[0].id == 93353083
    assert filtered_vacancies[1].id == 92223756


def test_filter_by_salary_correct_input(vacancies_obj_list: list[Vacancy]) -> None:
    """Проверяем корректность фильтрации по диапазону зарплат"""
    filtered_vacancies = filter_by_salary(vacancies_obj_list, "25000-30000")
    assert len(filtered_vacancies) == 1
    assert filtered_vacancies[0].id == 93353083


def test_filter_by_salary_empty_input(vacancies_obj_list: list[Vacancy]) -> None:
    """Проверяем выбрасывание исключения, если диапазон зарплат не введен пользователем"""
    with pytest.raises(InputException, match="Введите значения: 'от' и 'до'"):
        filter_by_salary(vacancies_obj_list, "")


def test_filter_by_salary_one_value(vacancies_obj_list: list[Vacancy]) -> None:
    """Проверяем выбрасывание исключения, если пользователь ввел только одно значение"""
    filtered_vacancies = filter_by_salary(vacancies_obj_list, "32000")
    assert len(filtered_vacancies) == 2
    assert filtered_vacancies[0].id == 92223756
    assert filtered_vacancies[1].id == 92223870


def test_filter_by_salary_one_value_no_matches(vacancies_obj_list: list[Vacancy]) -> None:
    """Проверяем выбрасывание исключения, если пользователь ввел одно значение и совпадений нет"""
    with pytest.raises(
        InputException, match="Вакансий с такой зарплатой не найдено. Попробуйте поискать что-нибудь другое."
    ):
        filter_by_salary(vacancies_obj_list, "50000")


def test_filter_by_salary_if_from_higher_than_to(vacancies_obj_list: list[Vacancy]) -> None:
    """Проверяем выбрасывание исключения, если значение 'от' больше, чем 'до'"""
    with pytest.raises(InputException, match="Значение 'от' не может быть больше значения 'до'"):
        filter_by_salary(vacancies_obj_list, "1000000-500000")


def test_filter_by_salary_incorrect_input(vacancies_obj_list: list[Vacancy]) -> None:
    """Проверяем выбрасывание исключения, если пользователь ввел данные не в том формиате"""
    with pytest.raises(InputException, match="Неверный формат ввода. Введите данные в формате 'от'-'до'"):
        filter_by_salary(vacancies_obj_list, "от 10000 до 200000")


def test_filter_by_salary_no_matches(vacancies_obj_list: list[Vacancy]) -> None:
    """Проверяем корректность фильтрации, если пользователь ввел одно значение"""
    with pytest.raises(
        InputException, match="Вакансий с такой зарплатой не найдено. Попробуйте поискать что-нибудь другое."
    ):
        filter_by_salary(vacancies_obj_list, "1000000-20000000")


def test_filter_by_words_no_keywords(vacancies_obj_list: list[Vacancy], no_keywords: list) -> None:
    """Проверяем вызов ошибки с заданным сообщением, если слова поиска не введены пользователем"""
    with pytest.raises(InputException, match="Введите слова для поиска."):
        filter_by_words(vacancies_obj_list, no_keywords)


def test_filter_by_words_bad_keywords(vacancies_obj_list: list[Vacancy], bad_keywords: list[str]) -> None:
    """Проверяем вызов ошибки с заданным сообщением, если по словам поиска от пользователя вакансии не найдены"""
    with pytest.raises(InputException, match="Вакансий с таким описанием не найдено"):
        filter_by_words(vacancies_obj_list, bad_keywords)


def test_sort_vacancies(vacancies_obj_list: list[Vacancy]) -> None:
    """Проверяем корректность сортировки вакансий по размеру зарплаты"""
    sorted_vacancies = sort_vacancies(vacancies_obj_list)
    assert len(sorted_vacancies) == 3
    assert sorted_vacancies[0].id == 92223756
    assert sorted_vacancies[1].id == 92223870
    assert sorted_vacancies[2].id == 93353083


def test_get_top_vacancies(vacancies_obj_list: list[Vacancy]) -> None:
    """Проверяем корректность выборки топ-n вакансий"""
    sorted_vacancies = sort_vacancies(vacancies_obj_list)
    top_vacancies = get_top_vacancies(sorted_vacancies, 2)
    assert len(top_vacancies) == 2
    assert top_vacancies[0].id == 92223756
    assert top_vacancies[1].id == 92223870
