from unittest.mock import patch, Mock
import pytest
import requests

from src.head_hunter_api import HeadHunter
from src.vacancy import Vacancy


def test_hh_obj_init(hh_obj: HeadHunter) -> None:
    assert hh_obj.url == "https://api.hh.ru/vacancies"
    assert hh_obj.headers == {"User-Agent": "HH-User-Agent"}
    assert hh_obj.params == {"text": "", "page": 0, "per_page": 100, "area": 113}
    assert hh_obj.vacancies == []

@patch("requests.get")
def test_status_code_raise_exception(mock_get, hh_obj ):
    response = mock_get.return_value.json_return_value
    response.status_code = 503
    with pytest.raises(requests.exceptions.RequestException):
        hh_obj.public_baseapi__connect_api()



