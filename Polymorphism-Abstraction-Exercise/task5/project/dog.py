import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\Polymorphism-Abstraction-Exercise\\task5\\project')

from project.animal import Animal


class Dog(Animal):

    @staticmethod
    def make_sound():
        return "Woof!"