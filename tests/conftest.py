import pytest

from src.head_hunter_api import HeadHunter


@pytest.fixture
def hh_obj() -> HeadHunter:
    """Фикстура для тестирования инициализации объекта класса 'HeadHunter'"""
    return HeadHunter()

