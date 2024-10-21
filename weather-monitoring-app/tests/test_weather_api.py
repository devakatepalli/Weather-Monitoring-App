import unittest
from weather_api import kelvin_to_celsius

class TestWeatherAPI(unittest.TestCase):
    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(kelvin_to_celsius(300), 26.85, places=2)

if __name__ == '__main__':
    unittest.main()
