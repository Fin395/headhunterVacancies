def filter_by_words(vacancies: list, words: list) -> list:
    vacancies_filtered_by_words = []
    for word in words:
        for vacancy in vacancies:
            if word in vacancy.requirements.lower():
                vacancies_filtered_by_words.append(vacancy)
    return vacancies_filtered_by_words

def filter_by_salary(vacancies_list: list, salary_range: str) -> list:
    salary_range_from = int(salary_range.split("-")[0])
    salary_range_to = int(salary_range.split("-")[1])
    vacancies_filtered_by_salary = list(filter(lambda x: salary_range_to >= x >= salary_range_from, vacancies_list))
    return vacancies_filtered_by_salary

def sort_vacancies(list_vacancies_objects: list) -> list:
    sorted_vacancies = sorted(list_vacancies_objects, key=lambda x: x.salary, reverse = True)
    return sorted_vacancies
