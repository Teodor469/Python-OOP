import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\Inheritence\\task5\\project')
from project.animal import Animal


class Dog(Animal):
    def bark(self):
        return "barking..."