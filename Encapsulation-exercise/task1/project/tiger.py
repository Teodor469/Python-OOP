import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\Encapsulation-exercise\\task1\\project')

from project.animal import Animal

class Tiger(Animal):

    def __init__(self, name, gender, age) -> None:
        super().__init__(name, gender, age, 45)