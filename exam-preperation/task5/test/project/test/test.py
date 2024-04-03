from project.robot import Robot
from unittest import TestCase, main

class TestRobot(TestCase):
    def setUp(self) -> None:
        self.robot = Robot(111, "Military", 100, 1000)
        self.other_robot = Robot(1111, "Education", 1000, 900)


    def test_correct_init(self):
        self.assertEqual(self.robot.robot_id, 111)
        self.assertEqual(self.robot.category, "Military")
        self.assertEqual(self.robot.available_capacity, 100)
        self.assertEqual(self.robot.price, 1000)
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])


    def test_category_if_allowed(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.category = "InvalidCategory"
        self.assertEqual(str(ex.exception), f"Category should be one of '{self.robot.ALLOWED_CATEGORIES}'")


    def test_if_price_is_negative(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.price = -1
        self.assertEqual(str(ex.exception), "Price cannot be negative!")

    
    def test_upgrade_successful(self):
        # Test scenario where the upgrade is successful
        initial_price = self.robot.price
        result = self.robot.upgrade("Improved Sensors", 300)
        
        self.assertEqual(result, f"Robot {self.robot.robot_id} was upgraded with Improved Sensors.")
        self.assertIn("Improved Sensors", self.robot.hardware_upgrades)
        self.assertEqual(len(self.robot.hardware_upgrades), 1)
        self.assertAlmostEqual(self.robot.price, initial_price + 300 * self.robot.PRICE_INCREMENT)


    def test_if_upgrade_is_not_possible(self):
        existing_component = "CPU"
        self.robot.hardware_upgrades.append(existing_component)
        
        # Attempt to upgrade with the same component
        initial_upgrade_list = self.robot.hardware_upgrades
        result = self.robot.upgrade(existing_component, 200)
        
        # Assert that the upgrade was not successful and the state remains unchanged
        self.assertEqual(result, f"Robot {self.robot.robot_id} was not upgraded.")
        self.assertEqual(initial_upgrade_list, self.robot.hardware_upgrades)
        self.assertEqual(len(self.robot.hardware_upgrades), 1)  # Check if the component count is still the same


    def test_update_no_existing_updates(self):
    # Test scenario where the robot has no existing software updates
        initial_capacity = self.robot.available_capacity
        result = self.robot.update(1.0, 50)
        
        self.assertEqual(result, f"Robot {self.robot.robot_id} was updated to version 1.0.")
        self.assertEqual(self.robot.software_updates, [1.0])
        self.assertEqual(self.robot.available_capacity, initial_capacity - 50)

    def test_update_existing_updates(self):
        # Test scenario where the robot has existing software updates
        self.robot.software_updates = [1.0, 2.0]
        initial_capacity = self.robot.available_capacity
        result = self.robot.update(3.0, 50)
        
        self.assertEqual(result, f"Robot {self.robot.robot_id} was updated to version 3.0.")
        self.assertEqual(self.robot.software_updates, [1.0, 2.0, 3.0])
        self.assertEqual(self.robot.available_capacity, initial_capacity - 50)

    def test_update_insufficient_capacity(self):
        # Test scenario where the robot doesn't have sufficient capacity for the update
        self.robot.software_updates = [1.0]
        initial_capacity = self.robot.available_capacity
        result = self.robot.update(2.0, 150)
        
        self.assertEqual(result, f"Robot {self.robot.robot_id} was not updated.")
        self.assertEqual(self.robot.software_updates, [1.0])
        self.assertEqual(self.robot.available_capacity, initial_capacity)

    def test_update_version_not_greater(self):
        # Test scenario where the provided version is not greater than existing software versions
        self.robot.software_updates = [2.0]
        initial_capacity = self.robot.available_capacity
        result = self.robot.update(2.0, 50)
        
        self.assertEqual(result, f"Robot {self.robot.robot_id} was not updated.")
        self.assertEqual(self.robot.software_updates, [2.0])
        self.assertEqual(self.robot.available_capacity, initial_capacity)


    def test_gt_if_other_robot_is_cheaper(self):
        result = self.robot.__gt__(self.other_robot)
        self.assertTrue(result)
        self.assertEqual(result, f'Robot with ID {self.robot.robot_id} is more expensive than Robot with ID {self.other_robot.robot_id}.')

    
    def test_get_if_price_is_the_same(self):
        self.other_robot = Robot(1111, "Education", 1000, 1000)
        result = self.robot.__gt__(self.other_robot)
        self.assertTrue(result)
        self.assertEqual(result, f'Robot with ID {self.robot.robot_id} costs equal to Robot with ID {self.other_robot.robot_id}.')
    
    
    def test_get_if_other_robot_is_more_expensive(self):
        self.other_robot = Robot(1111, "Education", 1000, 1100)
        result = self.robot.__gt__(self.other_robot)
        self.assertTrue(result)
        self.assertEqual(result, f'Robot with ID {self.robot.robot_id} is cheaper than Robot with ID {self.other_robot.robot_id}.')




if __name__ == '__main__':
    main()