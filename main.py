from head_hunter_api import HeadHunter
from src.vacancy_processing import Vacancy

if __name__ == "__main__":
    hh = HeadHunter()
    vacancies = hh.get_vacancies("python")
    vacancies_obj = Vacancy.from_dict(vacancies)








    for i in vacancies_obj:
        print(i)

