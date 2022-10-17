import unittest
from sentiment_analysis import mood_analysis

class TestMoodAnalysisFunction(unittest.TestCase):
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
