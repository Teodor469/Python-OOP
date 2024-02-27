import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\Inheritence\\task4\\project')
from project.vehicle import Vehicle


class Car(Vehicle):
    def drive(self):
        return "driving..."