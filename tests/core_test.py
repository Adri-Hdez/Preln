from Preln.preprocessing import (
    accents,
    lowercasing,
    punctuation_es,
    numbers_cleanner,
    stopwords_es,
    date,
    tokenizer,
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
        text = "hola Adrián"
        test = stopwords_es(text=text, debug=False) 

        self.assertEqual(test, "Adrián")

    def test_date(self):
        text = "14-01-2020"
        test = date(text=text, type="month", debug=False)

        self.assertEqual(test, "Enero")
    
    def test_tokenizer(self):
        text = "Hola, Adrián"
        test = tokenizer(text=text, debug=False)

        self.assertEqual(test, ["Hola",",","Adrián"])


if __name__ == "__main__":
    unittest.main()
