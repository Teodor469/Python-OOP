import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\Polymorphism-Abstraction-Exercise\\task6\\project')

from project.formula_teams.red_bull_team import RedBullTeam
from project.formula_teams.mercedes_team import MercedesTeam

class F1SeasonApp:
    def __init__(self) -> None:
        self.red_bull_team = None
        self.mercedes_team = None


    def register_team_for_season(self, team_name, budget):
        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)
        elif team_name == "Mercedes":
            self.mercedes_team = MercedesTeam(budget)
        else:
            raise ValueError("Invalid team name!")
        

        return f"{team_name} has joined the new F1 season."
    

    def new_race_results(self, race_name, red_bull_position, mercedes_position):
        if not self.red_bull_team or not self.mercedes_team:
            raise Exception("Not all teams have registered for the season.")
        return self.get_race_results(race_name, red_bull_position, mercedes_position)
        
    def get_race_results(self, race_name, red_bull_position, mercedes_position):
        ahead_team = "Red Bull" if red_bull_position < mercedes_position else "Mercedes"

        red_bull_revenue = self.red_bull_team.calculate_revenue_after_race(red_bull_position)
        mercedes_revenue = self.mercedes_team.calculate_revenue_after_race(mercedes_position)

        return (f"Red Bull: {red_bull_revenue}. Mercedes: {mercedes_revenue}. {ahead_team} is ahead at the {race_name} race.")