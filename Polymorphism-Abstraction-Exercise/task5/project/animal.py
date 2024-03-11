from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    @staticmethod
    @abstractmethod
    def make_sound():
        ...


    def __repr__(self) -> str:
        return f"This is {self.name}. {self.name} is {self.age} year old {self.gender} {self.__class__.__name__}"