import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\Polymorphism-Abstraction-Exercise\\task4\\project')

from project.animals.animal import Bird
from typing import List, Type
from project.food import Meat, Fruit, Vegetable, Seed

class Owl(Bird):

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.25


    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):

    @property
    def food_that_eats(self):
        return [Meat, Fruit, Vegetable, Seed]

    @property
    def gained_weight(self):
        return 0.35
    

    def make_sound(self):
        return "Cluck"