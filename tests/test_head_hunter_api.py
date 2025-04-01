def test_hh_obj_init(hh_obj):
    assert hh_obj.url == "https://api.hh.ru/vacancies"
    assert hh_obj.headers == {"User-Agent": "HH-User-Agent"}
    assert hh_obj.params == {"text": "", "page": 0, "per_page": 100, "area": 113}
    assert hh_obj.vacancies == []
