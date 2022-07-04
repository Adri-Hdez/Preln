import logging
import pandas as pd
from pathlib import Path
import csv

path = Path(__file__).parent / "./_external/stopwords.csv"

class Stopwords:
    """
    Stopwords handler.
    
    :param DEBUG: Pipeline methods info.
    :type DEBUG: bool
    """
    
    def __init__(self, debug=False):
        self.__debug = debug
    
    def append(self, words):
        """
        Method for adding a new word or words to the stopwords file.
        
        :param words: The stopword/s
        :type words: str
        """
        
        if self.__debug: logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)8s | %(message)s')
        if not ((isinstance(words, str)) or (isinstance(words, list))):
          logging.basicConfig(level=logging.ERROR, format='%(asctime)s | %(levelname)8s | %(message)s')
          logging.error('-- words variable type should be "str" or "list".')
          return

        if isinstance(words, str):
          with open(path, 'a', newline='', encoding='utf-8') as stopwords_file:
            fieldname = ['stopwords']
            writer = csv.DictWriter(stopwords_file, fieldnames=fieldname)
            writer.writerow({'stopwords': words})

        if isinstance(words, list):
          with open(path, 'a', newline='', encoding='utf-8') as stopwords_file:
            fieldname = ['stopwords']
            writer = csv.DictWriter(stopwords_file, fieldnames=fieldname)
            for word in words:
              writer.writerow({'stopwords': word})
        
        logging.debug('-- stopword/s added!')
    
    def delete(self, words):
        """
        Method for delete an existing word or words to the stopwords file.
        
        :param words: The stopword/s
        :type words: str
        """
        
        if self.__debug: logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)8s | %(message)s')
        if not ((isinstance(words, str)) or (isinstance(words, list))):
          logging.basicConfig(level=logging.ERROR, format='%(asctime)s | %(levelname)8s | %(message)s')
          logging.error('-- words variable type should be "str" or "list".')
          return

        if isinstance(words, str):
          df = pd.read_csv(path)
          df = pd.read_csv(path)['stopwords'].tolist()
          df.remove(words)

          with open(path, 'w', newline='', encoding='utf-8') as stopwords_file:
            fieldnames = ['stopwords']
            writer = csv.DictWriter(stopwords_file, fieldnames=fieldnames)
            writer.writeheader()
            for stopword in df:
              writer.writerow({'stopwords': stopword})

        if isinstance(words, list):
          df = pd.read_csv(path)
          df = pd.read_csv(path)['stopwords'].tolist()

          for word in words:
            df.remove(word)

          with open(path, 'w', newline='', encoding='utf-8') as stopwords_file:
            fieldnames = ['stopwords']
            writer = csv.DictWriter(stopwords_file, fieldnames=fieldnames)
            writer.writeheader()
            for stopword in df:
              writer.writerow({'stopwords': stopword})
        
        logging.debug('-- stopword/s deleted!')
        

    
    def info(self, lang='en'):
        """
        Displays information about the object and its methods.
        
        :param lang: Information language
        :type text: str
        """

        logging.basicConfig(level=logging.INFO, format='%(levelname)8s | %(message)s')
        if lang == 'es':
            logging.info('Bienvenido/a a la librería Preln, a continuación te daremos información de como funciona la clase Stopwords.')
            print('La clase funciona como un manejador de stopwords, es decir, lo que podrás hacer es añadir o eliminar la/s stopwords que desees.\n',
                  'Para hacer eso, tienes que hacer uso de los métodos "append" o "delete" pasándoles una stopword(str) o stopwords(list).\n')
            print('Muchas gracias por utilizar Preln en tus proyectos, cualquier comentario u opinión es de ayuda!')
            logging.info('Si quieres leer esto en otro idioma puedes cambiarlo desde los parámetros -> lang="en".')
        elif lang == 'en':
            logging.info('Welcome to the Preln library, here is some information on how the Stopwords class works.')
            print('The class works as a stopword handler, i.e. you can add or remove the stopword(s) you want.\n',
                  'To do that, you have to make use of the "append" or "delete" methods by passing them a stopword(str) or stopwords(list).\n')
            print('Thank you very much for using Preln in your projects, any feedback is helpful!')
            logging.info('If you want to read this in another language you can change it from the parameters -> lang="en".')
        else:
            logging.info('Welcome to the Preln library, here is some information on how the Stopwords class works.')
            logging.info('Before we start, at the moment only the information is implemented in English and Spanish, apologies for that. We will show you the information in English in order to reach as many people as possible.')
            print('The class works as a stopword handler, i.e. you can add or remove the stopword(s) you want.\n',
                  'To do that, you have to make use of the "append" or "delete" methods by passing them a stopword(str) or stopwords(list).\n')
            print('Thank you very much for using Preln in your projects, any feedback is helpful!')
            logging.info('If you want to read this in another language you can change it from the parameters -> lang="en".')