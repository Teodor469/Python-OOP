from typing import List
from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.passenger_car import PassengerCar
from project.vehicles.cargo_van import CargoVan


class ManagingApp:

    VEHICLE_TYPE = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self) -> None:
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []


    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."
        
        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"


    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VEHICLE_TYPE:
            return f"Vehicle type {vehicle_type} is inaccessible."
        
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."
            
        vehicle_class = self.VEHICLE_TYPE[vehicle_type]
        new_vehicle = vehicle_class(brand, model, license_plate_number)

        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."


    def allow_route(self, start_point: str, end_point: str, length: float):
        # Check if there is already a route with the same start point, end point, and length
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point:
                if route.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."
                elif route.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."
                else:
                    # Lock the longer route
                    route.is_locked = True

        # Create a new route id by counting the already added routes and adding 1
        route_id = len(self.routes) + 1
        # Create a new route instance
        new_route = Route(start_point, end_point, length, route_id)
        # Add the new route to the routes list
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."


    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int, is_accident_happened: bool):
        # Find the user with the given driving license number
        user = next((user for user in self.users if user.driving_license_number == driving_license_number), None)
        if not user or user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        # Find the vehicle with the given license plate number
        vehicle = next((vehicle for vehicle in self.vehicles if vehicle.license_plate_number == license_plate_number), None)
        if not vehicle or vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        # Find the route with the given route id
        route = next((route for route in self.routes if route.route_id == route_id), None)
        if not route or route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        # Drive the specific vehicle on the specific route
        vehicle.drive(route.length)
        # Change the vehicle's is_damaged status if an accident happened
        if is_accident_happened:
            vehicle.is_damaged = True
            # Decrease the user's rating if an accident happened
            user.decrease_rating()
        else:
            # Increase the user's rating if no accident happened
            user.increase_rating()

        # Return actual information about the vehicle after making the trip
        status = "OK" if not vehicle.is_damaged else "Damaged"
        return f"{vehicle.brand} {vehicle.model} License plate: {license_plate_number} Battery: {vehicle.battery_level}% Status: {status}"
        


    def repair_vehicles(self, count: int):
        # Filter damaged vehicles
        damaged_vehicles = [vehicle for vehicle in self.vehicles if vehicle.is_damaged]
        # Sort damaged vehicles alphabetically by brand and then by model
        damaged_vehicles.sort(key=lambda vehicle: (vehicle.brand, vehicle.model))
        # Select the first 'count' damaged vehicles or all if 'count' is greater than the number of damaged vehicles
        vehicles_to_repair = damaged_vehicles[:count]

        # Repair and recharge the selected vehicles
        for vehicle in vehicles_to_repair:
            vehicle.is_damaged = False
            vehicle.battery_level = 100

        count_of_repaired_vehicles = len(vehicles_to_repair)
        return f"{count_of_repaired_vehicles} vehicles were successfully repaired!"


    def users_report(self):
        # Sort users by rating in descending order
        sorted_users = sorted(self.users, key=lambda user: user.rating, reverse=True)

        # Generate the report string
        report = "*** E-Drive-Rent ***\n"
        for user in sorted_users:
            report += str(user) + "\n"

        return report