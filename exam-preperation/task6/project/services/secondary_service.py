from project.services.base_service import BaseService


class SecondaryService(BaseService):

    INITIAL_CAPACITY = 15

    def __init__(self, name: str) -> None:
        super().__init__(name, capacity = self.INITIAL_CAPACITY)


    def details(self):
        if not self.robots:
            return f"{self.name} Secondary Service:\nRobots: none"
        else:
            robot_names = ' '.join(robot.name for robot in self.robots)
            return f"{self.name} Secondary Service:\nRobots: {robot_names}"
