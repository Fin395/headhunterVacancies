import pytest

from src.exception import InputException
from src.utils import filter_by_words, sort_vacancies, get_top_vacancies
from src.vacancy import Vacancy


def test_filter_by_words(vacancies_obj_list, keywords_for_filter):
     filtered_vacancies = filter_by_words(vacancies_obj_list, keywords_for_filter)
     assert len(filtered_vacancies) == 2
     assert filtered_vacancies[0].id == 93353083
     assert filtered_vacancies[1].id == 92223756


def test_filter_by_words_no_keywords(vacancies_obj_list, no_keywords):
    with pytest.raises(InputException, match="Введите слова для поиска."):
        filter_by_words(vacancies_obj_list, no_keywords)


def test_filter_by_words_bad_keywords(vacancies_obj_list, bad_keywords):
    with pytest.raises(InputException, match="Вакансий с таким описанием не найдено"):
        filter_by_words(vacancies_obj_list, bad_keywords)


def test_sort_vacancies(vacancies_obj_list):
    sorted_vacancies = sort_vacancies(vacancies_obj_list)
    assert len(sorted_vacancies) == 3
    assert sorted_vacancies[0].id == 92223756
    assert sorted_vacancies[1].id == 92223870
    assert sorted_vacancies[2].id == 93353083


def test_get_top_vacancies(vacancies_obj_list):
    sorted_vacancies = sort_vacancies(vacancies_obj_list)
    top_vacancies = get_top_vacancies(sorted_vacancies, 2)
    assert len(top_vacancies) == 2
    assert top_vacancies[0].id == 92223756
    assert top_vacancies[1].id == 92223870


