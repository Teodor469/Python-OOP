import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\exam-preperation\\task1\\project')
from project.peaks.base_peak import BasePeak
from project.climbers.base_climber import BaseClimber


class SummitClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name)
        self.strength = 150
        self.conquered_peaks = []


    def can_climb(self) -> bool:
        return self.strength >= 75
    

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Advanced":
            self.strength -= 30 * 1.3
        else:
            self.strength -= 30 * 2.5

        if self.can_climb():
            self.conquered_peaks.append(peak.name)