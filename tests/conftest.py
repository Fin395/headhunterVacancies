import pytest

from src.head_hunter_api import HeadHunter
from src.vacancy import Vacancy


@pytest.fixture
def hh_obj() -> HeadHunter:
    """Фикстура для тестирования инициализации объекта класса 'HeadHunter'"""
    return HeadHunter()


@pytest.fixture
def first_vacancy():
    return Vacancy(93353083, "Тестировщик комфорта квартир", {"from": 350000, "to": 450000}, "https://hh.ru/employer/3499705", "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением...")

@pytest.fixture
def second_vacancy():
    return Vacancy(92223756, "Удаленный диспетчер чатов (в Яндекс)", {"from": 30000, "to": 44000}, "https://hh.ru/employer/9498120", "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением...")


@pytest.fixture
def vacancy_none_salary():
    return Vacancy(93353083, "Тестировщик комфорта квартир", None, "https://hh.ru/employer/3499705", "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением...")


@pytest.fixture
def vacancy_from_salary():
    return Vacancy(93353083, "Тестировщик комфорта квартир", {"from": 350000, "to": None}, "https://hh.ru/employer/3499705", "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением...")


@pytest.fixture
def vacancy_to_salary():
    return Vacancy(93353083, "Тестировщик комфорта квартир", {"from": None, "to": 450000}, "https://hh.ru/employer/3499705", "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением...")


@pytest.fixture
def vacancy_none_requirement():
    return Vacancy(93353083, "Тестировщик комфорта квартир", {"from": 350000, "to": None}, "https://hh.ru/employer/3499705", None)


@pytest.fixture
def list_of_vacancies_dict():
    return [
        {
            "id": "93353083",
            "name": "Тестировщик комфорта квартир",
            "salary":
                {
                    "from": 350000,
                    "to": 450000,
                    "currency": "RUR",
                    "gross": False
                },
            "alternate_url": "https://hh.ru/employer/3499705",
            "snippet":
                {
                    "requirement": "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением...",
                    "responsibility": "Оценивать вид из окна: встречать рассветы на кухне, и провожать алые закаты в спальне. Оценивать инфраструктуру района: ежедневно ходить на..."
                }
        },
        {
            "id": "92223756",
            "name": "Удаленный диспетчер чатов (в Яндекс)",
            "salary":
                {
                    "from": 30000,
                    "to": 44000,
                    "currency": "RUR",
                    "gross": True
                },
            "alternate_url": "https://hh.ru/employer/9498120",
            "snippet":
                {
                    "requirement": "Способен работать в команде. Способен принимать решения самостоятельно. Готов учиться и узнавать новое. Опыт работы в колл-центре или службе...",
                    "responsibility": "Работать с клиентами или партнерами для решения разнообразных ситуаций. Совершать звонки по их обращениям и давать письменные ответы. "
                }
        }
    ]



