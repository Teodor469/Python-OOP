import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\Encapsulation-exercise\\task4\\project')

from project.food.dessert import Dessert

class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name, price, grams, calories) -> None:
        super().__init__(name, Cake.PRICE, Cake.GRAMS, Cake.CALORIES)