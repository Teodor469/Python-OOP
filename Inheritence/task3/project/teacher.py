import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\Inheritence\\task3\\project')
from project.person import Person
from project.employee import Employee


class Teacher(Person, Employee):

    def teach(self):
        return f"teaching..."