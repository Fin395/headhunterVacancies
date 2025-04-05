import json
import pytest
from unittest.mock import mock_open, patch, Mock

from config import DEFAULT_JSON
from src.file import FileManager


def test_file_init_default(filename_default) -> None:
    """Проверяем корректность инициализации объекта класса FileManager"""
    assert filename_default.name == r'C:\Users\Sergei\PycharmProjects\headhunterVacancies\data\json_file.json'

def test_file_init_custom(filename_custom) -> None:
    """Проверяем корректность инициализации объекта класса FileManager"""
    assert filename_custom.name == "my_json_file.json"

def test_saving_vacancies_no_duplicates(filename_default, vacancies_obj_list, vacancies_obj_list_with_duplicate):
    with open(filename_default.name, "r", encoding="utf-8") as f:
        filename_default.add_to_file(vacancies_obj_list)
    with open(filename_default.name, "r", encoding="utf-8") as f:
        new_data = json.load(f)
        assert len(new_data) == 3
    with open(filename_default.name, "r", encoding="utf-8") as f:
        filename_default.add_to_file(vacancies_obj_list_with_duplicate)
    with open(filename_default.name, "r", encoding="utf-8") as f:
        new_data = json.load(f)
        assert len(new_data) == 4


def test_getting_from_file(filename_default, capsys: pytest.CaptureFixture):
    mocked_open = mock_open(read_data='[{"id": 93353083, "name": "Тестировщик комфорта квартир", "requirement": "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением...", "salary": 25000, "url": "https://hh.ru/employer/3499705"}, {"id": 92223756, "name": "Удаленный диспетчер чатов (в Яндекс)", "requirement": "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением...", "salary": 44000, "url": "https://hh.ru/employer/9498120"}]')
    with patch("builtins.open", mocked_open):
        filename_default.get_from_file()
    captured = capsys.readouterr()
    assert "{'id': 93353083, 'name': 'Тестировщик комфорта квартир', 'requirement': 'Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением...', 'salary': 25000, 'url': 'https://hh.ru/employer/3499705'}" in captured.out

def test_removal(filename_default):
    mocked_open = mock_open(
        read_data='[{"id": 93353083, "name": "Тестировщик комфорта квартир", "requirement": "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением...", "salary": 25000, "url": "https://hh.ru/employer/3499705"}, {"id": 92223756, "name": "Удаленный диспетчер чатов (в Яндекс)", "requirement": "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением...", "salary": 44000, "url": "https://hh.ru/employer/9498120"}]')
    with patch("builtins.open", mocked_open):
        result = filename_default.remove_from_file()
    assert result is None
