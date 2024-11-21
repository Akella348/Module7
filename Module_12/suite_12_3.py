import unittest
import runner
from tests_12_3 import Runnertest, TournamentTest

suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Runnertest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner_ = unittest.TextTestRunner(verbosity=2)
runner_.run(suite)

