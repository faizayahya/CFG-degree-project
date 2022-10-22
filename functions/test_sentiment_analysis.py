# Aaliya

from unittest import TestCase, main
from unittest.mock import patch
from ..functions.sentiment_analysis import *


class TestMoodAnalysisFunction(TestCase):
    def test_positive_sentiment(self):
        my_input = "very good"
        result = mood_analysis(my_input)
        self.assertGreaterEqual(result, 0.05)

    def test_negative_sentiment(self):
        my_input = "very bad"
        result = mood_analysis(my_input)
        self.assertLessEqual(result, -0.05)

    def test_neutral_sentiment(self):
        my_input = "okay"
        result = mood_analysis(my_input)
        self.assertAlmostEqual(result, 0, places=0)

    def test_invalid_input(self):
        my_input = "verry goood"
        with self.assertRaises(Exception):
            mood_analysis(my_input)

    def test_spelling_mistake(self):
        my_input = "verry goood"
        with self.assertRaises(Exception):
            mood_analysis(my_input)


class TestAPICallFunction(TestCase):

    def test_valid_url(self):
        my_input = 'good'
        self.assertEqual(mood_analysis_api(my_input).status_code, 200)

    @patch('..sentiment_analysis.mood_analysis_api')
    def test_exception(self, mock_get):
        mock_get.return_value.status_code != 200
        self.assertRaises(requests.exceptions.RequestException)


if __name__ == "__main__":
    main()
