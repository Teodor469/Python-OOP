from typing import List
from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:

    DELICACY_TYPES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    BOOTH_TYPES = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self) -> None:
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0.0 #NOTE total income of the pastry shop


    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if self.find_delicacies_by_name(name):
            raise Exception(f"{name} already exists!")
        
        if type_delicacy not in self.DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        
        new_delicacy = self.DELICACY_TYPES[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."


    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if self.find_booth_by_number(booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")
        
        if type_booth not in self.BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")
        
        new_booth = self.BOOTH_TYPES[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."


    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        raise Exception(f"No available booth for {number_of_people} people!")
    

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.find_booth_by_number(booth_number)
        delicacy = self.find_delicacies_by_name(delicacy_name)

        if booth not in self.booths:
            raise Exception(f"Could not find booth {booth_number}!")
        
        if delicacy not in self.delicacies:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."


    def leave_booth(self, booth_number: int):
        booth = self.find_booth_by_number(booth_number)

        total_bill = booth.price_for_reservation
        for delicacy in booth.delicacy_orders:
            total_bill += delicacy.price

        self.income += total_bill

        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0.0

        return f"Booth {booth_number}:\nBill: {total_bill:.2f}lv."


    def get_income(self):
        return f"Income: {self.income:.2f}lv."


    #helper methods

    def find_delicacies_by_name(self, delicacy_name):
        for delicacy in self.delicacies:
            if delicacy.name == delicacy_name:
                return delicacy
        return None
    
    def find_booth_by_number(self, booth_number):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                return booth
        return None