class Vacancy:
    __slots__ = ("name", "url", "salary", "requirements")

    def __init__(self, name, url, salary, requirements):
        self.name = name
        self.url = url
        self.salary = salary
        self.__validate_salary(salary)
        self.requirements = requirements
        self.__validate_requirement(requirements)

    def __str__(self):
        return f"Вакансия: {self.name}, ссылка на вакансию: {self.url}, зарплата: {self.salary}, требования: {self.requirements}"

    def __le__(self, other):
        if isinstance(self.salary, other):
            return self.salary <= other

    def __ge__(self, other):
        if isinstance(self.salary, other):
            return self.salary >= other


    @classmethod
    def from_dict(cls, vacancies):
        vacancy_obj_list = []
        for vacancy in vacancies:
            name, url, salary, requirements = vacancy["name"], vacancy["url"], vacancy["salary"], vacancy["snippet"]["requirement"]
            vacancy_obj_list.append(cls(name, url, salary, requirements))
        return vacancy_obj_list

    def __validate_salary(self, salary):
        if salary is None:
            self.salary = 0
        elif isinstance(salary, dict):
            if not salary["from"] is None and not salary["to"] is None:
                self.salary =salary["to"]
            elif not salary["from"] is None and salary["to"] is None:
                self.salary = salary["from"]
            else:
                self.salary = salary["to"]
        return self.salary

    def __validate_requirement(self, requirements):
        if requirements is None:
            self.requirements = "Не указано"
        return self.requirements





