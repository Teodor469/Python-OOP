import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\Polymorphism-Abstraction-Exercise\\task5\\project')

from project.cat import Cat


class Tomcat(Cat):

    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Male")

    @staticmethod
    def make_sound() -> str:
        return "Hiss"