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

