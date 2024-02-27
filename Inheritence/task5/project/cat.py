import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\Inheritence\\task5\\project')
from project.animal import Animal


class Cat(Animal):
    def meow(self):
        return "meowing..."