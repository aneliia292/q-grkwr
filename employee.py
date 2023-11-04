class Employee:

    def __init__(self, name, age, salary, bonus):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = bonus


def get_name(self):
    return self.__name


def get_age(self):
    return self.__age


def get_salary(self):
    return self.__salary


def set_bonus(self, bonus):
    self.__bonus = bonus


def get_bonus(self):
    return self.__bonus


def get_total_salary(self):
    return self.__salary + self.__bonus


employee = Employee ("John Smith", 30, 5000, 1000)

name = employee.get_name ()
age = employee.get_age ()
salary = employee.get_salary ()
bonus = employee.get_bonus ()
total_salary = employee.get_total_salary ()

print ("Name:", name)
print ("Age:", age)
print ("Salary:", salary)
print ("Bonus:", bonus)
print ("Total Salary:", total_salary)
