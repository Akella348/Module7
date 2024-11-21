import runner_added as runner
import unittest
import logging
from tests_12_3 import Runnertest, TournamentTest

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')

class Runnertest(unittest.TestCase):
    @unittest.skipIf(False, 'Тест заморожен')
    def test_walk(self):
        try:
            walker = runner.Runner('Bolt', -10)
            walker.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)

    @unittest.skipIf(False, 'Тест заморожен')  # Условие декоратора
    def test_run(self):
        try:

            sprinter = runner.Runner(123, 10)
            sprinter.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)

if __name__ == 'main':
    unittest.main()
