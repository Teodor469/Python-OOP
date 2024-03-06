import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\Encapsulation-exercise\\task4\\project')

from project.food.starter import Starter


class Soup(Starter):
    def __init__(self, name: str, price: float, grams: float):
        super().__init__(name, price, grams)