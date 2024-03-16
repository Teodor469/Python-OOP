import sys
sys.path.append('C:\\Users\\lifet\\Documents\\GitHub\\Python-OOP\\exam-preperation\\task1\\project')
from project.peaks.base_peak import BasePeak

from abc import ABC, abstractmethod


class BaseClimber(ABC):
    def __init__(self, name: str, strength: float, conquered_peaks: list, is_prepared: bool) -> None:
        if name == "":
            raise ValueError("Climber name cannot be null or empty!")
        if strength <= 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self.name = name
        self.strength = strength
        self.conquered_peaks = conquered_peaks
        self.is_prepared = True


    @abstractmethod
    def can_climb():
        pass


    @abstractmethod
    def climb(peak: BasePeak):
        pass


    def rest(self):
        self.strength += 15


    def __str__(self) -> str:
        return f"{self.__class__.__name__}: /// Climber name: {self.name} * Left strength: {self.strength:.1f} * Conquered peaks: {', '.join(self.conquered_peaks)} ///"