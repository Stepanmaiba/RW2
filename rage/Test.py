import unittest
from rage.Werehouse import Werehouse
from rage.Office import Office
from rage.Rezidential import Rezidential


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.test_werehouse = Werehouse()
        self.test_office = Office()
        self.test_rezidential = Rezidential()

    def test_werehouse(self):
        self.assertEqual(self.test_werehouse.size_werehouse(), '/n')

    def test_office(self):
        self.assertEqual(self.test_office.size_office(), '/n')

    def test_residential(self):
        self.assertEqual(self.test_rezidential.size_residential(), '/n')


if __name__ == "__main__":
  unittest.main()