class Product:
    def __init__(self, name, quantity) -> None:
        self.name = name
        self.quantity = quantity


    def increase(self, quantity):
        self.quantity += quantity


    def decrease(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity


    def __repr__(self) -> str:
        return self.name