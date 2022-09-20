from Pipeln.pipeline import Pipeline
from .core.lowercasing import lowercasing
from .core.numbers import numbers_cleanner
from .core.punctuation import punctuation_es
from .core.stopwords import stopwords_es
from .core.accents import accents
from .core.date import date
from .core.tokenizer import tokenizer
import logging
import pandas as pd
import numpy as np
import os

class Preprocessing:
    """
    Instanciate a preprocessing pipeline for text in spanish.
    Text will be returned vectorized.

    :param date: Give format or eliminate dates.
    :type date: bool

    :param date_format: Type of format.
    :type date_format: str

    :param accents: Eliminate accents.
    :type accents: bool
    
    :param lowercasing: Lowering the text.
    :type lowercasing: bool
    
    :param numbers: Delete numbers from text.
    :type numbers: bool

    :param punctuation: Eliminate puntuation.
    :type punctuation: bool

    :param stopwords: Eliminate stopwords.
    :type stopwords: bool
    
    :param DEBUG: Pipeline methods info.
    :type DEBUG: bool
    """
    
    def __init__(self, date=False, date_format=None, accents=False, lowercasing=True, numbers=True, punctuation=True, stopwords=True, tokenizer=True, debug=False):
        self.__date = date
        self.__date_format = date_format
        self.__accents = accents
        self.__lowercasing = lowercasing
        self.__numbers = numbers
        self.__debug = debug
        self.__punctuation = punctuation
        self.__stopwords = stopwords
        self.__tokenizer = tokenizer
    
    def pipeline(self, text):
        """
        Preprocesses a given text by
        applying the different preprocessing methods
        
        :param text: The text to be preprocessed
        :type text: str
        
        :return: Preprocessed text
        :rtype: str
        """
        
        if self.__debug: logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)8s | %(message)s')
        logging.debug('> Starting preprocessing pipeline...')
                
        # Pipeline creation
        if self.__date: text = date(text=text, type=self.__date_format, debug=self.__debug)
        if self.__accents: text = accents(text=text, debug=self.__debug)
        if self.__lowercasing: text = lowercasing(text=text, debug=self.__debug)
        if self.__numbers: text = numbers_cleanner(text=text, debug=self.__debug)
        if self.__punctuation: text = punctuation_es(text=text, debug=self.__debug)
        if self.__stopwords: text = stopwords_es(text=text, debug=self.__debug)
        if self.__tokenizer: text = tokenizer(text=text, debug=self.__debug)
        
        logging.debug('Preprocessing pipeline completed! <')
        logging.debug('')
        
        return text
    
    def pipelineFile(self, file, textCol):
        """
        Preprocesses a given file by
        applying the different preprocessing methods
        
        :param file: The file to be preprocessed
        :type file: file
        
        :param textCol: The text column to be preprocessed
        :type textCol: string
        
        :param fileType: The type of the file
        :type fileType: string
        
        :return: Preprocessed file
        :rtype: file
        """
        
        if self.__debug: logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)8s | %(message)s')
        logging.debug('> Starting preprocessing pipeline...')
        
        split_path = os.path.splitext(file)
        ext = split_path[1].replace('.', '')

        if ext == 'csv': df = pd.read_csv(file)
        if ext == 'xml': df = pd.read_xml(file)
        if ext == 'excel': df = pd.read_excel(file)
        if ext == 'json': df = pd.read_json(file)
        
        texts = df[textCol].values.tolist()
        array = []

        for text in texts: 
            text = self.pipeline(text)   
            array.append(text)
        
        logging.debug('Preprocessing pipeline completed! <')
        logging.debug('')
        
        return array
    
    def write(self, inputArray, originalFile = None, outputFile = './preprossedText.csv'):
        """
        Preprocesses a given file by
        applying the different preprocessing methods
        
        :param inputArray: Input array
        :type inputArray: array
        
        :param originalFile: File raw content
        :type originalFile: file
        
        :param fileType: The type of the file
        :type fileType: string
        
        :param outputFile: Output file
        :type outputFile: csv
        """
        
        if self.__debug: logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)8s | %(message)s')
        logging.debug('> Creating new file...')
        
        if originalFile == None:
            df = pd.DataFrame(inputArray, columns=['text'])
            df.to_csv(outputFile, index=False)
        else:
            split_path = os.path.splitext(originalFile)
            ext = split_path[1].replace('.', '')

            if ext == 'csv': df = pd.read_csv(originalFile)
            if ext == 'xml': df = pd.read_xml(originalFile)
            if ext == 'excel': df = pd.read_excel(originalFile)
            if ext == 'json': df = pd.read_json(originalFile)

            df['preprocessed_text'] = inputArray
            df.to_csv(originalFile, index=False)
            
        logging.debug(f' {outputFile} file created! <')
        logging.debug('')
    
    def info(self, lang='en'):
        """
        Displays information about the library and its methods.
        
        :param lang: Information language
        :type text: str
        """

        logging.basicConfig(level=logging.INFO, format='%(levelname)8s | %(message)s')
        if lang == 'es':
            logging.info('Bienvenido/a a la librería Preln, a continuación te daremos información de como funciona.')
            print('Ahora mismo Preprocessing cuenta con 2 métodos, el de información (el actual) y el de pipeline.\n',
                  'Dentro del método de pipeline vas a poder ejecutar una secuencia de métodos que aplicaran un preprocesado a tu texto, de normal están todos activos menos el de eliminación de fechas y acentos.\n',
                  'Para activarlos simplemente ponlo como "True" -> date="True" a través de los parámetros. También podrás activar los mensajes de debug de la misma forma.')
            print('Muchas gracias por utilizar Preln en tus proyectos, cualquier comentario u opinión es de ayuda!')
            logging.info('Si quieres leer esto en otro idioma puedes cambiarlo desde los parámeotros -> lang="en".')
        if lang == 'en':
            logging.info('Welcome to the Preln package, here is some information on how it works.')
            print('At the moment Preprocessing has 2 methods, the information method (the current one) and the pipeline method.\n',
                  'Within the pipeline method you will be able to execute a sequence of methods that will apply a preprocessing to your text, normally all of them are active except the one for removing dates and accents.\n',
                  'To enable them simply set it to "True" -> date="True" via the parameters. You can also enable debug messages in the same way.')
            print('Thank you very much for using Preln in your projects, any feedback is helpful!')
            logging.info('If you want to read this in another language you can change it from the parameters -> lang="en".')
        else:
            logging.info('Welcome to the Preln package, here is some information on how it works.')
            logging.info('Before we start, at the moment only the information is implemented in English and Spanish, apologies for that. We will show you the information in English in order to reach as many people as possible.')
            print('At the moment Preprocessing has 2 methods, the information method (the current one) and the pipeline method.\n',
                  'Within the pipeline method you will be able to execute a sequence of methods that will apply a preprocessing to your text, normally all of them are active except the one for removing dates and accents.\n',
                  'To enable them simply set it to "True" -> date="True" via the parameters. You can also enable debug messages in the same way.')
            print('Thank you very much for using Preln in your projects, any feedback is helpful!')
            logging.info('If you want to read this in another language you can change it from the parameters -> lang="en".')