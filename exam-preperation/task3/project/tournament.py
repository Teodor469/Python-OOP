from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.outdoor_team import OutdoorTeam
from project.teams.indoor_team import IndoorTeam


class Tournament:
    def __init__(self, name: str, capacity: int) -> None:
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value


    def add_equipment(self, equipment_type: str):
        pass


    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        pass


    def sell_equipment(self, equipment_type: str, team_name: str):
        pass


    def remove_team(self, team_name: str):
        pass

    
    def increase_equipment_price(self, equipment_type: str):
        pass


    def play(self, team_name1: str, team_name2: str):
        pass


    def get_statistics(self):
        pass