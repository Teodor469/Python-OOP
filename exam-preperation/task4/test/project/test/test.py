from second_hand_car import SecondHandCar
from unittest import TestCase, main

class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car = SecondHandCar("Civic", "Sedan", 50000, 15000.50)

    def test_init_valid_data(self):
        car = SecondHandCar("Civic", "Sedan", 50000, 15000.50)
        self.assertEqual(car.model, "Civic")
        self.assertEqual(car.car_type, "Sedan")
        self.assertEqual(car.mileage, 50000)
        self.assertEqual(car.price, 15000.50)
        self.assertEqual(car.repairs, [])

    def test_init_invalid_price_zero(self):
        with self.assertRaises(ValueError) as error:
            SecondHandCar("CR-V", "SUV", 20000, 0.0)
        self.assertEqual(str(error.exception), "Price should be greater than 1.0!")

    def test_init_invalid_price_negative(self):
        with self.assertRaises(ValueError) as error:
            SecondHandCar("Corolla", "Sedan", 35000, -10.25)
        self.assertEqual(str(error.exception), "Price should be greater than 1.0!")

    def test_init_invalid_mileage_brand_new(self):
        with self.assertRaises(ValueError) as error:
            SecondHandCar("Prius", "Hybrid", 50, 22000.00)
        self.assertEqual(str(error.exception), "Please, second-hand cars only! Mileage must be greater than 100!")

    def test_set_promotional_price_valid_discount(self):
        car = SecondHandCar("Yaris", "Hatchback", 80000, 12500.75)
        message = car.set_promotional_price(10000.00)
        self.assertEqual(car.price, 10000.00)
        self.assertEqual(message, "The promotional price has been successfully set.")

    def test_set_promotional_price_invalid_increase(self):
        car = SecondHandCar("Camry", "Sedan", 42000, 18500.25)
        with self.assertRaises(ValueError) as error:
            car.set_promotional_price(20000.00)
            self.assertEqual(str(error.exception), "You are supposed to decrease the price!")

    def test_need_repair_valid_repair(self):
        car = SecondHandCar("RAV4", "SUV", 78000, 21000.99)
        message = car.need_repair(3500.50, "Engine oil change")
        self.assertEqual(car.price, 24501.49)
        self.assertEqual(car.repairs, ["Engine oil change"])
        self.assertEqual(message, "Price has been increased due to repair charges.")

    def test_need_repair_expensive_repair(self):
        car = SecondHandCar("Tacoma", "Truck", 120000, 16800.00)
        message = car.need_repair(9000.75, "Transmission replacement")
        self.assertEqual(car.price, 16800.00)
        self.assertEqual(car.repairs, [])
        self.assertEqual(message, "Repair is impossible!")

    # def test_gt_different_car_types(self):
    #     car1 = SecondHandCar("Accord", "Sedan", 65000, 14200.40)
    #     car2 = SecondHandCar("Pilot", "SUV", 90000, 20000.00)
    #     with self.assertRaises(TypeError) as error:
    #         car1 > car2
    #     self.assertEqual(str(error.exception), "Cars cannot be compared. Type mismatch!")

    def test_gt_higher_price(self):
        car1 = SecondHandCar("HR-V", "SUV", 32000, 17800.15)  # Set mileage for car1
        car2 = SecondHandCar("Odyssey", "Minivan", 58000, 17800.15)  # Set mileage for car2
        self.assertTrue(car1 > car2)

if __name__ == '__main__':
    main()