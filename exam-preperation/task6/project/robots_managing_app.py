from typing import List
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService
from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot



class RobotsManagingApp:

    SERVICE_TYPES = {"MainService": MainService, "SecondaryService": SecondaryService}
    ROBOT_TYPES = {"FemaleRobot": FemaleRobot, "MaleRobot": MaleRobot}

    def __init__(self) -> None:
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []


    def add_service(self, service_type: str, name: str):
        if service_type not in self.SERVICE_TYPES:
            raise Exception("Invalid service type!")
        
        new_service = self.SERVICE_TYPES[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."


    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.ROBOT_TYPES:
            raise Exception("Invalid robot type!")
        
        new_robot = self.ROBOT_TYPES[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."


    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.find_robot_by_name(robot_name)
        service = self.find_service_by_name(service_name)

        if isinstance(robot, FemaleRobot) and not isinstance(service, SecondaryService):
            return f"Unsuitable service."
        elif isinstance(robot, MaleRobot) and not isinstance(service, MainService):
            return f"Unsuitable service."
        

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")
        
        self.robots.remove(robot)
        service.robots.append(robot)

        return f"Successfully added {robot_name} to {service_name}."


    def remove_robot_from_service(self, robot_name: str, service_name: str):
        robot = self.find_robot_by_name(robot_name)
        service = self.find_service_by_name(service_name)

        if robot not in service.robots:
            raise Exception("No such robot in this service!")
        
        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."


    def feed_all_robots_from_service(self, service_name: str):
        service = self.find_service_by_name(service_name)

        number_of_robots_fed = 0
        for robot in service.robots:
            robot.eating()
            number_of_robots_fed += 1

        return f"Robots fed: {number_of_robots_fed}."


    def service_price(self, service_name: str):
        service = self.find_service_by_name(service_name)

        total_price = sum(robot.price for robot in service.robots)
        return f"The value of service {service_name} is {total_price:.2f}."


    def __str__(self):
        result = ""
        for service in self.services:
            result += str(service) + "\n"
        return result
    

    #Helper methods

    def find_robot_by_name(self, robot_name):
        for robot in self.robots:
            if robot.name == robot_name:
                return robot
        return None
    

    def find_service_by_name(self, service_name):
        for service in self.services:
            if service.name == service_name:
                return service
        return None