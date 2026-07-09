import unittest
from src.ship import Ship

class TestShip(unittest.TestCase):
    def test_info(self):
        s = Ship(\"Test\", 100)
        self.assertEqual(s.info(), \"Ship: Test, Length: 100m\")

if __name__ == \"__main__\":
    unittest.main()
