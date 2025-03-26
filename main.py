from head_hunter_api import HeadHunter
from src.utils import filter_by_salary, sort_vacancies, filter_by_words
from src.vacancy_processing import Vacancy


hh_api = HeadHunter()


def user_interaction():
    user_search_query = input("Введите ключевое слово для поиска вакансий: ") # Пример: "python"
    hh_vacancies = hh_api.get_vacancies(user_search_query)
    vacancies_list = Vacancy.from_dict(hh_vacancies)
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").lower().split()
    filtered_vacancies = filter_by_words(vacancies_list, filter_words)
    user_salary_range = input("Укажите диапазон зарплат (в формате 'от'-'до'): ") # Пример: 100000 - 150000
    try:
        ranged_vacancies = filter_by_salary(filtered_vacancies, user_salary_range)
    except ValueError as e:
        print(f"{e}")
    else:
        sorted_vacancies = sort_vacancies(ranged_vacancies)



    # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # print_vacancies(top_vacancies)
        for vacancy in sorted_vacancies:
            print(vacancy)

if __name__ == "__main__":
    user_interaction()
