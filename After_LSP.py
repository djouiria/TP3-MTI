from abc import ABC, abstractmethod

# Base class: only what is common to everyone
class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

# Separate abstraction for people who work
class Employee(Person, ABC):
    @abstractmethod
    def get_salary(self):
        pass

    @abstractmethod
    def assign_task(self, task):
        pass

class Worker(Employee):
    def get_salary(self):
        return 3000

    def assign_task(self, task):
        print(f"{self.name} got task: {task}")

class Student(Person):
    def study(self):
        print(f"{self.name} is studying")

# Client code
def process_employee(emp: Employee):
    print(emp.get_salary())
    emp.assign_task("Prepare report")

def show_name(person: Person):
    print(person.get_name())

if __name__ == '__main__':
    w = Worker("Ahmed")
    s = Student("Sara")

    process_employee(w)   # صحيح
    show_name(w)          # صحيح
    show_name(s)          # صحيح، الطالب يحل محل Person بأمان
    s.study()