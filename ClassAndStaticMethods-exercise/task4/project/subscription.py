import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\ClassAndStaticMethods-exercise\\task3\\project')
from project.next_id_mixin import NextIdMixin



class Subscription(NextIdMixin):
    id = 1

    def __init__(self, date, customer_id, trainer_id, exercise_id) -> None:
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = self.get_next_id()
        self.increment_id()


    def __repr__(self) -> str:
        return f"Subscription <{self.id}> on {self.date}"