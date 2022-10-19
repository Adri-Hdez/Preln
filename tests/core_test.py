from Preln.preprocessing import (
    accents,
    lowercasing,
    punctuation_es,
    numbers_cleanner,
    stopwords_es,
    date,
)
import unittest

# ----------------------------------- Core methods testing units -----------------------------------
class TestCore(unittest.TestCase):
    def test_accents(self):
        text = "Hola, Adrián!"
        test = accents(text=text, debug=False)

        self.assertEqual(test, "Hola, Adrian!")

    def test_lowercasing(self):
        text = "Hola, Adrián!"
        test = lowercasing(text=text, debug=False)

        self.assertEqual(test, "hola, adrián!")

    def test_punctuation(self):
        text = "Hola, Adrián!"
        test = punctuation_es(text=text, debug=False)

        self.assertEqual(test, "Hola Adrián")

    def test_numbers(self):
        text = "Hola, 2323Adrián2323!"
        test = numbers_cleanner(text=text, debug=False)

        self.assertEqual(test, "Hola, Adrián!")

    def test_stopwords(self):
        text = "Hola Adrián"
        test = stopwords_es(
            text=text, debug=False
        )  # Check method failure, only using the package it works correctly

        self.assertEqual(test, "Adrián")

    def test_date(self):
        text = "14-01-2020"
        test = date(text=text, type="month", debug=False)

        self.assertEqual(test, "Enero")


if __name__ == "__main__":
    unittest.main()
