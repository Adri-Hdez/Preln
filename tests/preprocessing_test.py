from Preln.preprocessing import Preprocessing
import unittest

# ----------------------------------- Preprocessing testing units -----------------------------------
class TestPreprocessing(unittest.TestCase):
    def test_pipeline(self):
        text = "Hola, Adrián!"
        preprocessor = Preprocessing(accents=True)
        test = preprocessor.pipeline(text=text)

        self.assertEqual(test, ["adrian"])

    def test_filePipeline(self):
        preprocessor = Preprocessing(accents=True)
        test = preprocessor.filePipeline("./__testsDatafiles/sample.csv", "Welcome")

        self.assertEqual(test, [["adrian"]])

    def test_write(self):
        # This test cannot be done because write method is not returnable
        pass


if __name__ == "__main__":
    unittest.main()
