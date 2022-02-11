import datetime
now = datetime.datetime.now()

class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def check_salary(self, *args):
        for i in args:
            if isinstance(i, int):
                return self.salary * i
            if i == 'y':
                return now.day*self.salary

    def work(self):
        return 'I come to the office.'
    def __lt__(self, other):
        return self.salary < other.salary
    def __le__(self, other):
        return self.salary <= other.salary
    def __gt__(self, other):
        return self.salary > other.salary
    def __ge__(self, other):
        return self.salary >= other.salary
    def __eq__(self, other):
        return self.salary == other.salary
    def __ne__(self, other):
        return self.salary != other.salary

class Recruiter(Employee):
    def work(self):
        return super().work().replace('.', '') + ' and start to hiring.'

    def __str__(self):
        return f'{type(self).__name__}:{self.name}'

class Programmer(Employee):
    def __init__(self, name, salary, tech_stack):
        super().__init__(name, salary)
        self.tech_stack = tech_stack

    def lt(self, other):
        return len(self.tech_stack) < len(other.tech_stack)
    def le(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)
    def gt(self, other):
        return len(self.tech_stack) > len(other.tech_stack)
    def ge(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)
    def eq(self, other):
        return len(self.tech_stack) == len(other.tech_stack)
    def ne(self, other):
        return len(self.tech_stack) != len(other.tech_stack)

    def work(self):
        return super().work().replace('.', '') + ' and start to coding.'
    def __str__(self):
        return f'{type(self).__name__}:{self.name}'

    def __add__(self, other):
        return Programmer(self.name, self.salary, set(self.tech_stack + other.tech_stack))

class Candidate:
    def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade


class Vacancy:
    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level
