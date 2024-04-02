from project.second_hand_car import SecondHandCar
from unittest import TestCase, main

class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar("Toyota", "Sedan", 50000, 10000.0)
        self.other_car = SecondHandCar("Nissan", "SUV", 60000, 12000.0)

    
    def test_correct_init(self):
        self.assertEqual(self.car.model, "Toyota")
        self.assertEqual(self.car.car_type, "Sedan")
        self.assertEqual(self.car.mileage, 50000)
        self.assertEqual(self.car.price, 10000.0)
        self.assertEqual(self.car.repairs, [])


    def test_check_if_price_is_greater_than_one(self):
        with self.assertRaises(ValueError) as ex:
            self.car.price = 1.0
        self.assertEqual(str(ex.exception), 'Price should be greater than 1.0!')


    def test_check_if_mileage_is_too_low(self):
        with self.assertRaises(ValueError) as ex:
            self.car.mileage = 100
        self.assertEqual(str(ex.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

    
    def test_promotional_price_higher(self):
        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(10001.0)
        self.assertEqual(str(ex.exception), 'You are supposed to decrease the price!')

    
    def test_promotional_price_lower(self):
        result = self.car.set_promotional_price(9999.9)
        self.assertEqual(result, 'The promotional price has been successfully set.')


    def test_if_the_repair_is_more_expensive_than_half_the_price_of_the_car(self):
        initial_price = self.car.price
        result = self.car.need_repair(5001.0, "Replace brakes")
        self.assertEqual(result, 'Repair is impossible!')  # Assert against return value
        self.assertEqual(self.car.price, initial_price)  # Assert price remains unchanged
        self.assertEqual(len(self.car.repairs), 0)  # Assert repairs list is unchanged



    def test_if_the_repair_is_less_expensive_than_half_the_price_of_the_car(self):
        initial_price = self.car.price
        result = self.car.need_repair(4999.0, "Replace brakes")
        self.assertEqual(result, 'Price has been increased due to repair charges.')  # Assert against return value
        self.assertEqual(self.car.price, initial_price + 4999.0)  # Assert price is updated correctly
        self.assertEqual(len(self.car.repairs), 1)  # Assert repairs list contains the repair description


    def test_gt_if_cars_are_not_same(self):
        result = self.car.__gt__(self.other_car)
        self.assertEqual(result, 'Cars cannot be compared. Type mismatch!')


    def test_get_if_cars_are_same(self):
        result = self.car.__gt__(self.other_car)
        self.assertTrue(result)
        self.assertTrue(self.car > self.other_car)
        self.assertTrue(self.other_car > self.car)


    def test_str_message(self):
        result = self.car.__str__()
        self.assertEqual(result, f"""Model {self.car.model} | Type {self.car.car_type} | Milage {self.car.mileage}km
Current price: {self.car.price:.2f} | Number of Repairs: {len(self.car.repairs)}""")



if __name__ == '__main__':
    main()