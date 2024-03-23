import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\exam-preperation\\task1\\project')
from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):
    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)


    def calculate_difficulty_level(self) -> int:
        if self.elevation > 2500:
            return 'Extreme'
        elif 1500 <= self.elevation <= 2500:
            return "Advanced"
        
    
    def get_recommended_gear(self) -> list:
        return ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]