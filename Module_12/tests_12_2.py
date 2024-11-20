import runner
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    def setUp(self):
        self.runner_1 = runner.Runner('Усейн', 10)
        self.runner_2 = runner.Runner('Андрей', 9)
        self.runner_3 = runner.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results.keys()):
            print(cls.all_results[key])

    def test_tournament_1(self):
        tournament = runner.Tournament(90, self.runner_1, self.runner_3)
        results = tournament.start()
        self.all_results[1] = {place: participant.name for place, participant in results.items()}
        self.assertTrue(self.all_results[1][2] == self.runner_3.name)

    def test_tournament_2(self):
        tournament = runner.Tournament(90, self.runner_2, self.runner_3)
        results = tournament.start()
        self.all_results[2] = {place: participant.name for place, participant in results.items()}
        self.assertTrue(self.all_results[2][2] == self.runner_3.name)

    def test_tournament_3(self):
        tournament = runner.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = tournament.start()
        self.all_results[3] = {place: participant.name for place, participant in results.items()}
        self.assertTrue(self.all_results[3][3] == self.runner_3.name)

if __name__ == '__main__':
    unittest.main()

