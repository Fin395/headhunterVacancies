import pytest

from src.exception import InputException
from src.utils import filter_by_words
from src.vacancy import Vacancy


# def test_filter_by_words(vacancies_obj_list, keywords_for_filter):
#     result = filter_by_words(vacancies_obj_list, keywords_for_filter)
#     filtered_vacancy1 = Vacancy(93353083, "Тестировщик комфорта квартир", {"from": 350000, "to": 450000}, "https://hh.ru/employer/3499705", "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением...")
#     filtered_vacancy2 = Vacancy(92223756, "Удаленный диспетчер чатов (в Яндекс)", {"from": 30000, "to": 44000}, "https://hh.ru/employer/9498120", "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением...")
#     assert result == [filtered_vacancy1, filtered_vacancy2]

def test_filter_by_words_no_keywords(vacancies_obj_list, no_keywords):
    with pytest.raises(InputException, match="Введите слова для поиска."):
        filter_by_words(vacancies_obj_list, no_keywords)


def test_filter_by_words_bad_keywords(vacancies_obj_list, bad_keywords):
    with pytest.raises(InputException, match="Вакансий с таким описанием не найдено"):
        filter_by_words(vacancies_obj_list, bad_keywords)
