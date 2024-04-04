from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer("Teodor", 21, 100.0)
        self.other_player = TennisPlayer("Tanya", 21, 100.0)


    def test_init(self):
        self.assertEqual(self.player.name, "Teodor")
        self.assertEqual(self.player.age, 21)
        self.assertEqual(self.player.points, 100.0)
        self.assertEqual(self.player.wins, [])


    def test_check_if_name_is_more_than_two_symbols(self):
        with self.assertRaises(ValueError) as ex:
            self.player.name = "Te"
        self.assertEqual(str(ex.exception), "Name should be more than 2 symbols!")


    def test_check_if_player_is_18_years(self):
        with self.assertRaises(ValueError) as ex:
            self.player.age = 17
        self.assertEqual(str(ex.exception), "Players must be at least 18 years of age!")


    def test_if_tournament_name_is_not_unique(self):
        existing_tournament = "Australia Open"
        self.player.wins.append(existing_tournament)

        initial_tournament_list = self.player.wins
        result = self.player.add_new_win(existing_tournament)

        self.assertEqual(result, f"{existing_tournament} has been already added to the list of wins!")
        self.assertEqual(initial_tournament_list, self.player.wins)
        self.assertEqual(len(self.player.wins), 1)


    def test_if_tournament_name_is_unique(self):
        tournament = "French Open"
        result = self.player.add_new_win(tournament)

        self.assertIsNone(result)
        self.assertEqual(len(self.player.wins), 1)


    def test_lt_if_points_are_more_for_the_other_player(self):
        self.other_player.points = 101.0

        result = self.player.__lt__(self.other_player)
        self.assertEqual(result, f'{self.other_player.name} is a top seeded player and he/she is better than {self.player.name}')


    def test_lt_if_my_points_are_more(self):
        self.other_player.points = 99.0

        result = self.player.__lt__(self.other_player)
        self.assertEqual(result, f'{self.player.name} is a better player than {self.other_player.name}')


    def test_str_method(self):
        result = self.player.__str__()

        self.assertEqual(result, f"Tennis Player: {self.player.name}\n" \
               f"Age: {self.player.age}\n" \
               f"Points: {self.player.points:.1f}\n" \
               f"Tournaments won: {', '.join(self.player.wins)}")



if __name__ == "__main__":
    main()