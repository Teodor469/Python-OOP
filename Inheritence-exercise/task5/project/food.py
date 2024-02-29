import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\Inheritence-exercise\\task5\\project')
from project.product import Product

class Food(Product):
    def __init__(self, name) -> None:
        super().__init__(name, 15)