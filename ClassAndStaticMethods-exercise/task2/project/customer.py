import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\ClassAndStaticMethods-exercise\\task2\\project')


class Customer:
    def __init__(self, name, age, id) -> None:
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []


    def __repr__(self):
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({', '.join(d.name for d in self.rented_dvds)})"