def filter_by_words(vacancies: list, keywords: list) -> list:
    """Вспомогательная функция, которая фильтрует список вакансий по введенным пользователем ключевым словам"""
    vacancies_filtered_by_words = []
    for word in keywords:
        for vacancy in vacancies:
            if word in vacancy.requirements.lower():
                vacancies_filtered_by_words.append(vacancy)
    return vacancies_filtered_by_words


def filter_by_salary(vacancies_list: list, salary_range: str) -> list:
    """Вспомогательная функция, которая фильтрует список вакансий по диапазону зарплаты, полученного от пользователя"""
    if len(salary_range.split("-")) == 1 and [item.isdigit() for item in salary_range.split("-")]:
        salary_range_from = int(salary_range.split("-")[0])
        salary_range_to = salary_range_from
    elif len(salary_range.split("-")) != [1, 2] or [not item.isdigit() for item in salary_range.split("-")]:
        raise TypeError
    elif len(salary_range.split("-")) == 2 and [item.isdigit() for item in salary_range.split("-")]:
        salary_range_from = int(salary_range.split("-")[0])
        salary_range_to = int(salary_range.split("-")[1])
        if all(vacancy.salary < salary_range_from or vacancy.salary > salary_range_to for vacancy in vacancies_list ):
            raise ValueError
        elif any(salary_range_to >= vacancy >= salary_range_from for vacancy in vacancies_list):
            vacancies_filtered_by_salary = list(filter(lambda x: salary_range_to >= x >= salary_range_from, vacancies_list))
            return vacancies_filtered_by_salary


def sort_vacancies(list_vacancies_objects: list) -> list:
    """Вспомогательная функция, которая сортирует вакансии по зарплате от большего к меньшему"""

    sorted_vacancies = sorted(list_vacancies_objects, key=lambda x: x.salary, reverse = True)
    return sorted_vacancies
