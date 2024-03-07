import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\ClassAndStaticMethods-exercise\\task3\\project')
from project.next_id_mixin import NextIdMixin

class Customer(NextIdMixin):

    id = 1

    def __init__(self, name, address, email) -> None:
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()


    def __repr__(self) -> str:
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"