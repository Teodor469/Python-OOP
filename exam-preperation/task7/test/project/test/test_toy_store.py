from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.store = ToyStore()


    def test_toy_shelf_initialization(self):
        expected_shelf = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        self.assertDictEqual(self.store.toy_shelf, expected_shelf)

    def test_add_toy_to_non_existing_shelf(self):
        with self.assertRaises(Exception) as context:
            self.store.add_toy("Z", "Teddy Bear")
        self.assertEqual(str(context.exception), "Shelf doesn't exist!")

    def test_add_existing_toy_to_shelf(self):
        self.store.toy_shelf["A"] = "Teddy Bear"
        with self.assertRaises(Exception) as context:
            self.store.add_toy("A", "Teddy Bear")
        self.assertEqual(str(context.exception), "Toy is already in shelf!")

    def test_add_toy_to_taken_shelf(self):
        self.store.toy_shelf["A"] = "Doll"
        with self.assertRaises(Exception) as context:
            self.store.add_toy("A", "Teddy Bear")
        self.assertEqual(str(context.exception), "Shelf is already taken!")

    def test_add_toy_successfully(self):
        result = self.store.add_toy("B", "Car")
        self.assertEqual(result, "Toy:Car placed successfully!")
        self.assertEqual(self.store.toy_shelf["B"], "Car")

    def test_remove_toy_from_non_existing_shelf(self):
        with self.assertRaises(Exception) as context:
            self.store.remove_toy("Z", "Teddy Bear")
        self.assertEqual(str(context.exception), "Shelf doesn't exist!")

    def test_remove_non_existing_toy_from_shelf(self):
        with self.assertRaises(Exception) as context:
            self.store.remove_toy("A", "Doll")
        self.assertEqual(str(context.exception), "Toy in that shelf doesn't exists!")

    def test_remove_toy_successfully(self):
        self.store.add_toy("C", "Doll")

        self.assertEqual(self.store.toy_shelf["C"], "Doll")
        result = self.store.remove_toy("C", "Doll")
        self.assertEqual(result, "Remove toy:Doll successfully!")
        self.assertIsNone(self.store.toy_shelf["C"])



if __name__ == "__main__":
    main()