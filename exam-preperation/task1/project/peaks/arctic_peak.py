import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\exam-preperation\\task1\\project')
from project.peaks.base_peak import BasePeak

class ArcticPeak(BasePeak):
    def __init__(self, name, elevation) -> None:
        super().__init__(name, elevation)


    def calculate_difficulty_level(self) -> int:
        if self.elevation > 3000:
            return "Extreme"
        elif self.elevation >= 2000:
            return "Advanced"

    def get_recommended_gear(self) -> list:
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]