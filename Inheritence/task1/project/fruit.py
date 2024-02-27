import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\Inheritence\\task1\\project')

from project.food import Food


class Fruit(Food):
    def __init__(self, name, expiration_date) -> None:
        self.name = name
        super().__init__(expiration_date)