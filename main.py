from src.head_hunter_api import HeadHunter
from src.exception import InputException
from src.file import FileManager
from src.utils import filter_by_salary, sort_vacancies, filter_by_words, get_top_vacancies, from_vacancy_to_dict
from src.vacancy_processing import Vacancy


hh_api = HeadHunter()

def user_interaction():
    user_search_query = input("Введите ключевое слово для поиска вакансий: ") # Пример: "разработчик"
    try:
        hh_vacancies = hh_api.get_vacancies(user_search_query)
    except InputException as e:
        print(e)
    else:
        vacancies_list = Vacancy.from_dict(hh_vacancies)
        filter_words = input("Введите ключевые слова для фильтрации вакансий: ").lower().split() # Пример: "python java"
        try:
            filtered_vacancies = filter_by_words(vacancies_list, filter_words)
        except InputException as e:
            print(e)
        else:
            user_salary_range = input("Укажите диапазон зарплат (в формате 'от'-'до'): ") # Пример: 100000 - 150000
            try:
                ranged_vacancies = filter_by_salary(filtered_vacancies, user_salary_range)
            except InputException as e:
                print(e)
            else:
                sorted_vacancies = sort_vacancies(ranged_vacancies)
                try:
                    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
                except ValueError as e:
                    print(e)
                else:
                    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
                    return top_vacancies
                          # вывести вакансии пользователю

if __name__ == "__main__":

    user_vacancies = user_interaction()
    vacancies_dict = from_vacancy_to_dict(user_vacancies)
    mng = FileManager()
    mng.add_to_file(vacancies_dict)
    mng.get_from_file()

