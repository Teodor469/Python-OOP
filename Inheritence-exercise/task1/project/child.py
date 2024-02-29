import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\Inheritence-exercise\\task1\\project')
from project.person import Person

class Child(Person):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)