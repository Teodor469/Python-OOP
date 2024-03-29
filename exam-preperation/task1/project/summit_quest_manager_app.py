import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\exam-preperation\\task1\\project')
from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak
from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak

class SummitQuestManagerApp:
    CLIMBER_TYPES = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
    PEAK_TYPE = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}

    def __init__(self) -> None:
        self.climbers = []
        self.peaks = []


    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.CLIMBER_TYPES:
            return f"{climber_type} doesn't exist in our register."

        climber = self.find_climber(climber_name)
        if climber is not None:
            return f"{climber_name} has been already registered."

        new_climber = self.CLIMBER_TYPES[climber_type](climber_name)
        self.climbers.append(new_climber)
        return f"{climber_name} is successfully registered as a {climber_type}."
    

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.PEAK_TYPE:
            return f"{peak_type} is an unknown type of peak."

        new_peak = self.PEAK_TYPE[peak_type](peak_name, peak_elevation)
        self.peaks.append(new_peak)
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

        required_gear = set(peak.get_recommended_gear())
        missing_gear = required_gear - set(gear)

        if missing_gear:
            climber.is_prepared = False
            sorted_missing_gear = sorted(missing_gear)
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted_missing_gear)}."
        else:
            return f"{climber_name} is prepared to climb {peak_name}."
        
    
    def perform_climbing(self, climber_name: str, peak_name: str) -> str:
        climber = self.find_climber(climber_name)
        peak = self.find_peak(peak_name)

        if not climber:
            return f"Climber {climber_name} is not registered yet."
        
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."
        
        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)  # Attempt the climb (updates climber strength and conquered peaks)
            return f"{climber.name} conquered {peak.name} whose difficulty level is {peak.difficulty_level}."
        elif not climber.is_prepared:
            return f"{climber.name} will need to be better prepared next time."
        else:
            climber.rest()
            return f"{climber.name} needs more strength to climb {peak_name} and is therefore taking some rest."
        

    def get_statistics(self) -> str:
        sorted_climbers = sorted([climber for climber in self.climbers if climber.conquered_peaks],
                                 key=lambda climber: (-len(climber.conquered_peaks), climber.name))

        result = [
            f"Total climbed peaks: {len(self.peaks)}",
            "**Climber's statistics:**"
        ]

        climber_statistics = "\n".join(str(c) for c in sorted_climbers)
        result.append(climber_statistics)

        return '\n'.join(result)
    
    # def get_statistics(self) -> str:
    #     # Filter climbers who conquered at least one peak
    #     conquered_climbers = [climber for climber in self.climbers if climber.conquered_peaks]

    #     # Sort climbers by conquered peaks (descending) and then by name (ascending)
    #     conquered_climbers.sort(key=lambda c: (-len(c.conquered_peaks), c.name))

    #     # Build statistics string using str.join()
    #     stats = [f"Total climbed peaks: {sum(len(c.conquered_peaks) for c in conquered_climbers)}",
    #             "**Climber's statistics:**"]  # Start with total climbed peaks and header
    #     stats.extend(str(climber) for climber in conquered_climbers)  # Add each climber's statistics
    #     return '\n'.join(stats)
