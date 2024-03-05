import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\Encapsulation-exercise\\task4\\project')

from project.food.main_dish import MainDish


class Salmon(MainDish):
    GRAMS = 22

    def __init__(self, name, price, grams) -> None:
        super().__init__(name, price, Salmon.GRAMS)