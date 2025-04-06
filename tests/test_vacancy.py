from src.vacancy import Vacancy


def test_vacancy_init(first_vacancy: Vacancy) -> None:
    """Проверяем корректность инициализации экземпляра класса"""
    assert first_vacancy.id == 93353083
    assert first_vacancy.name == "Тестировщик комфорта квартир"
    assert first_vacancy.salary == 450000
    assert first_vacancy.url == "https://hh.ru/employer/3499705"
    assert first_vacancy.requirement == "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением..."

def test_vacancy_none_salary(vacancy_none_salary: Vacancy) -> None:
    """Проверяем валидацию значения атрибута 'salary', если None"""
    assert vacancy_none_salary.salary == 0

def test_vacancy_str(first_vacancy: Vacancy) -> None:
    """Проверяем корректность работы магического метода '__str__'"""
    assert str(first_vacancy) == "id вакансии: 93353083, наименование вакансии: Тестировщик комфорта квартир, зарплата: 450000, ссылка на вакансию: https://hh.ru/employer/3499705, требования: Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением..."

def test_vacancy_lt_and_gt(first_vacancy: Vacancy, second_vacancy: Vacancy) -> None:
    """Проверяем корректность работы магических методов '__lt__' и '__gt__'"""
    result1 = first_vacancy < second_vacancy
    result2 = first_vacancy > second_vacancy
    assert result1 is False
    assert result2 is True

def test_vacancy_from_dict(list_of_vacancies_dict: list[dict]) -> None:
    """Проверяем корректность преобразования вакансий из списка словарей в список объектов класса"""
    vacancies_obj_list = Vacancy.from_dict(list_of_vacancies_dict)
    assert vacancies_obj_list[0].id == "93353083"
    assert vacancies_obj_list[1].id == "92223756"

def test_vacancy_from_or_to_salary(vacancy_from_salary: Vacancy, vacancy_to_salary: Vacancy) -> None:
    """Проверяем корректность работы приватного метода валидации зарплаты '__validate_salary'"""
    assert vacancy_from_salary.salary == 350000
    assert vacancy_to_salary.salary == 450000


def test_vacancy_none_requirement(vacancy_none_requirement: Vacancy) -> None:
    """Проверяем корректность работы приватного метода валидации зарплаты '__validate_requirement'"""
    assert vacancy_none_requirement.requirement == "Не указано"

