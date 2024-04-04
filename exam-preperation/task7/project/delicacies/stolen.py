from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    GINGER_BREAD_PORTION = 250

    def __init__(self, name: str, price: float) -> None:
        super().__init__(name, self.GINGER_BREAD_PORTION, price)

    def details(self):
        return f"Stolen {self.name}: 250g - {self.price:.2f}lv."