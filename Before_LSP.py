class Person:
    def get_salary(self):
        return 3000

    def assign_task(self, task):
        print(f"Task assigned: {task}")

class Student(Person):
    def get_salary(self):
        raise Exception("Student has no salary")

    def assign_task(self, task):
        raise Exception("Student cannot be assigned tasks")

# Client code that expects a Person
def process(person: Person):
    print(person.get_salary())
    person.assign_task("Prepare report")

process(Person())    # Works correctly
process(Student())   # Raises an exception!