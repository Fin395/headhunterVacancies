def filter_by_salary(vacancies_list, salary_range):
    salary_range_from = int(salary_range.split("-")[0])
    salary_range_to = int(salary_range.split("-")[1])

    vacancies_filtered_by_salary = filter(lambda x: salary_range_to >= x >= salary_range_from, vacancies_list)
    return vacancies_filtered_by_salary

def sort_vacancies(list_vacancies_objects):
    sorted_vacancies = sorted(list_vacancies_objects, key=lambda x: x.salary, reverse = True)
    return sorted_vacancies


