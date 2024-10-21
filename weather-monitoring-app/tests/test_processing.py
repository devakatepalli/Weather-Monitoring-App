import unittest
from processing import process_weather_data

class TestProcessing(unittest.TestCase):

    def setUp(self):
        # Simulated weather data for testing
        self.weather_data = {
            'Delhi': {
                'weather': [{'main': 'Clear'}],
                'main': {'temp': 300, 'feels_like': 305},
                'dt': 1633545600
            },
            'Mumbai': {
                'weather': [{'main': 'Rain'}],
                'main': {'temp': 295, 'feels_like': 298},
                'dt': 1633549200
            }
        }

    def test_process_weather_data(self):
        daily_summary = process_weather_data(self.weather_data)

        # Assert that the summary for Delhi is calculated correctly
        delhi_summary = daily_summary['Delhi']
        self.assertAlmostEqual(delhi_summary['average_temp'], 26.85, places=2)  # Kelvin to Celsius
        self.assertEqual(delhi_summary['dominant_condition'], 'Clear')

        # Assert that the summary for Mumbai is calculated correctly
        mumbai_summary = daily_summary['Mumbai']
        self.assertAlmostEqual(mumbai_summary['average_temp'], 21.85, places=2)  # Kelvin to Celsius
        self.assertEqual(mumbai_summary['dominant_condition'], 'Rain')

    def test_empty_data(self):
        # Test how the system behaves with empty data
        empty_data = {}
        summary = process_weather_data(empty_data)
        self.assertEqual(len(summary), 0)

if __name__ == '__main__':
    unittest.main()
