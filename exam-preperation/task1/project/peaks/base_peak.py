from abc import ABC, abstractmethod

class BasePeak(ABC):
  def __init__(self, name: str, elevation: int):
    if len(name) < 2:
      raise ValueError("Peak name cannot be less than 2 symbols!")
    if elevation < 1500:
      raise ValueError("Peak elevation cannot be below 1500m.")
    self.name = name
    self.elevation = elevation
    self.difficulty_level = self.calculate_difficulty_level()  # Call the abstract method

  @abstractmethod
  def calculate_difficulty_level(self) -> int:
    pass  # Subclasses will implement this

  @abstractmethod
  def get_recommended_gear(self) -> list:
    pass  # Subclasses will implement this