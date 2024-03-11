import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\Polymorphism-Abstraction-Exercise\\task5\\project')

from project.cat import Cat

class Kitten(Cat):

    def __init__(self, name, age) -> None:
        super().__init__(name, age, "Female")


    @staticmethod
    def make_sound():
        return "Meow"