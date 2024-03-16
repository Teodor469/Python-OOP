import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\exam-preperation\\task1\\project')
from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak
from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak

class SummitQuestManagerApp:
    def __init__(self, climbers: list, peaks: list) -> None:
        self.climbers = climbers
        self.peaks = peaks


    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in ("ArcticClimber", "SummitClimber"):
            return f"{climber_type} doesn't exist in our register."
        elif climber_name in self.climbers:
            return f"{climber_name} has been already registered."
        

        if climber_type == "ArcticClimber":
            climber = ArcticClimber(climber_name)
        else:
            climber = SummitClimber(climber_name)

        self.climbers.append(climber)

        return f"{climber_name} is successfully registered as a {climber_type}."
    

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in ("ArcticPeak", "SummitPeak"):
            return f"{peak_type} is an unknown type of peak."
        
        if peak_type == "ArcticPeak":
            peak = ArcticPeak(peak_name, peak_elevation)
        else:
            peak = SummitPeak(peak_name, peak_elevation)
        self.peaks.append(peak)

        return f"{peak_name} is successfully added to the wish list as a {peak_type}."
    
    def find_climber(self, climber_name):
        for climber in self.climbers:
            if climber.name == climber_name:
                return climber
        return None  # Return None if climber not found

    def find_peak(self, peak_name):
        for peak in self.peaks:
            if peak.name == peak_name:
                return peak
        return None  # Return None if peak not found


    def check_gear(self, climber_name: str, peak_name: str, gear: list):
        climber = self.find_climber(climber_name)
        peak = self.find_peak(peak_name)

        if not climber or not peak:
            return ""
        
        recommender_gear = peak.get_recommended_gear()

        missing_gear = set(recommender_gear) - set(gear)

        if not missing_gear:
            climber.is_prepared = True
            return f"{climber_name} is prepared to climb {peak_name}."
        else:
            climber.is_prepared = False
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(missing_gear))}"
        
    
    def perform_climbing(self, climber_name: str, peak_name: str) -> str:
        climber = self.find_climber(climber_name)
        peak = self.find_peak(peak_name)

        if not climber:
            return f"Climber {climber_name} is not registered yet."
        elif not peak:
            return f"Peak {peak_name} is not part of the wish list."
        elif climber.can_climb(peak) and climber.is_prepared:
            climber.climb(peak)  # Attempt the climb (updates climber strength and conquered peaks)
            difficulty_level = peak.calculate_difficulty_level()
            return f"{climber.name} conquered {peak.name} whose difficulty level is {difficulty_level}."
        elif not climber.is_prepared:
            return f"{climber.name} will need to be better prepared next time."
        else:
            return f"{climber.name} needs more strength to climb {peak_name} and is therefore taking some rest."
        

    def get_statistics(self) -> str:
        # Filter climbers who conquered at least one peak
        conquered_climbers = [climber for climber in self.climbers if climber.conquered_peaks]

        # Sort climbers by conquered peaks (descending) and then by name (ascending)
        conquered_climbers.sort(key=lambda c: (-len(c.conquered_peaks), c.name))

        # Build statistics string
        stats = f"Total climbed peaks: {sum(len(c.conquered_peaks) for c in conquered_climbers)}\n**Climber's statistics:**\n"
        for climber in conquered_climbers:
            stats += f"{climber}\n"  # Use __str__ method of climber for formatted output

        return stats.rstrip()  # Remove trailing newline