from head_hunter_api import HeadHunter
from src.utils import filter_by_salary
from src.vacancy_processing import Vacancy, sort_vacancies

if __name__ == "__main__":
    hh_api = HeadHunter()
    hh_vacancies = hh_api.get_vacancies("python")
    vacancies_list = Vacancy.from_dict(hh_vacancies)
    ranged_vacancies = filter_by_salary(vacancies_list, "200000 - 300000")
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    for vacancy in sorted_vacancies:
        print(vacancy)



