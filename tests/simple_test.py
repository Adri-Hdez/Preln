from Preln.preprocessing import Preprocessing
import unittest

# ----------------------------------- Preprocessing testing units -----------------------------------
class TestPreprocessing(unittest.TestCase):
    def pipeline_test(self):
        preprocessor = Preprocessing(date=False, date_format=None, accents=False, lowercasing=True, privacy_format="multi:replace", correction=True, media=True, 
               media_format="mention:delete", numbers=False, punctuation=True, 
               stopwords=True, tokenizer=True, debug=False)

        sample_text = "¡Hola @usuario!, mi nombre es Preln, me han creado Adrián y Raúl. Revisa mi documentación en https://www.preln.org"
        test = preprocessor.pipeline(sample_text)
        self.assertEqual(test, ["adrian"])
        pass


if __name__ == "__main__":
    unittest.main()





# print(test) # ['MENTION', 'nombre', 'ORG', 'creado', 'PERSON', 'PERSON', 'revisa', 'documentación', 'URL']