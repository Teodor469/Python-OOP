from abc import ABC, abstractmethod
import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\Polymorphism-Abstraction-Exercise\\task4\\project')
from typing import List, Type
from project.food import Meat, Fruit, Vegetable, Seed

class Animal(ABC):
    def __init__(self, name, weight) -> None:
        self.name = name
        self.weight = weight
        self.food_eaten = 0


    @property
    @abstractmethod
    def food_that_eats(self):
        pass

    @property
    @abstractmethod
    def gained_weight(self):
        pass

    @abstractmethod
    def make_sound(self):
        ...

    def feed(self, food):
        if type(food) not in self.food_that_eats:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        
        self.weight += self.gained_weight * food.quantity
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size) -> None:
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region) -> None:
        super().__init__(name, weight)
        self.living_region = living_region


    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"