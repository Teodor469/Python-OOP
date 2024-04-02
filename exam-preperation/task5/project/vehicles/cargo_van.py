from project.vehicles.base_vehicle import BaseVehicle

class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180.00

    def __init__(self, brand: str, model: str, license_plate_number: str) -> None:
        super().__init__(brand, model, license_plate_number, max_mileage = self.MAX_MILEAGE)


    def drive(self, mileage: float):
        # Calculate the percentage of max mileage covered by the given mileage
        percentage = min((mileage / self.MAX_MILEAGE) * 100, 100)
        # Round the percentage to the closest integer
        percentage = round(percentage)

        # Reduce the battery level by the calculated percentage
        percentage_with_load = percentage - 5

        # Ensure that battery level does not go below 0
        self.battery_level = max(percentage_with_load, 0)