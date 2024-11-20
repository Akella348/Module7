import runner
import unittest

class Runnertest(unittest.TestCase):

    def test_walk(self):
        walker = runner.Runner('Bolt')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        sprinter = runner.Runner('Flash')
        for i in range(10):
            sprinter.run()
        self.assertEqual(sprinter.distance, 100)
    def test_challenge(self):
        walker = runner.Runner('Bolt')
        sprinter = runner.Runner('Flash')
        for i in range(10):
            walker.walk()
            sprinter.run()
        self.assertNotEqual(walker.distance, sprinter.distance)

if __name__ == '__main__':
    unittest.main()