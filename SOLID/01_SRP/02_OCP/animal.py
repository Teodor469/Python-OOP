from abc import ABC, abstractmethod


class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):
        pass

    def get_species(self):
        return self.__class__.__name__.lower()


class Cat(Animal):
    def make_sound(self):
        return "meow"
    

class Dog(Animal):
    def make_sound(self):
        return "woof"
    

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())