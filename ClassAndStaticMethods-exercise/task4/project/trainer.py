import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\ClassAndStaticMethods-exercise\\task3\\project')
from project.next_id_mixin import NextIdMixin


class Trainer(NextIdMixin):
    id = 1
    def __init__(self, name) -> None:
        self.name = name
        self.id = self.get_next_id()
        self.increment_id()

    def __repr__(self) -> str:
        return f"Trainer <{self.id}> {self.name}"