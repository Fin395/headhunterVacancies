from src.vacancy import Vacancy


def test_vacancy_init(first_vacancy):
    assert first_vacancy.id == 93353083
    assert first_vacancy.name == "Тестировщик комфорта квартир"
    assert first_vacancy.salary == 450000
    assert first_vacancy.url == "https://hh.ru/employer/3499705"
    assert first_vacancy.requirement == "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением..."


def test_vacancy_init_none_salary(first_vacancy_none_salary):
    assert first_vacancy_none_salary.id == 93353083
    assert first_vacancy_none_salary.name == "Тестировщик комфорта квартир"
    assert first_vacancy_none_salary.salary == 0
    assert first_vacancy_none_salary.url == "https://hh.ru/employer/3499705"
    assert first_vacancy_none_salary.requirement == "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением..."


def test_vacancy_str(first_vacancy):
    assert str(first_vacancy) == "id вакансии: 93353083, наименование вакансии: Тестировщик комфорта квартир, зарплата: 450000, ссылка на вакансию: https://hh.ru/employer/3499705, требования: Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением..."


def test_vacancy_lt_and_gt(first_vacancy, second_vacancy):
    result1 = first_vacancy < second_vacancy
    result2 = first_vacancy > second_vacancy
    assert result1 is False
    assert result2 is True


def test_vacancy_from_dict(list_of_vacancies_dict) -> None:
    vacancies_obj_list = Vacancy.from_dict(list_of_vacancies_dict)
    assert vacancies_obj_list[0].id == "93353083"
    assert vacancies_obj_list[1].id == "92223756"


