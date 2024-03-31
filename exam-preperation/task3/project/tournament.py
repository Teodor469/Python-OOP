from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.outdoor_team import OutdoorTeam
from project.teams.indoor_team import IndoorTeam


class Tournament:

    EQUIPMENT_TYPE = {"ElbowPad": ElbowPad, "KneePad":KneePad}
    TEAM_TYPE = {"OutdoorTeam":OutdoorTeam, "IndoorTeam":IndoorTeam}


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
        if equipment_type not in self.EQUIPMENT_TYPE:
            raise Exception("Invalid equipment type!")
        self.equipment.append(equipment_type)
        return f"{equipment_type} was successfully added."


    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.TEAM_TYPE:
            raise Exception("Invalid team type!")
        
        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."
        
        new_team = self.TEAM_TYPE[team_type](team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."
        


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