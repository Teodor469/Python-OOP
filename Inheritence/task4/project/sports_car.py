import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\Inheritence\\task4\\project')
from project.car import Car

class SportsCar(Car):
    def race(self):
        return "racing..."