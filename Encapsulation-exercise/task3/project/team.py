import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\Encapsulation-exercise\\task3\\project')
from project.player import Player

class Team:
    def __init__(self, name, rating) -> None:
        self.__name = name
        self.__rating = rating
        self.__players = []

    
    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {self.name} has already joined"
        self.__players.append(player)
        return f"Player {self.name} joined team {self.__name}"
    

    def remove_player(self, player_name):
        try:
            player = [p for p in self.__players if p.name == player_name][0]
            self.__players.remove(player)
            return player
        except IndexError:
            return f"Player {player_name} not found"