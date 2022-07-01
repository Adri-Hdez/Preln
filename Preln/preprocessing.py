from .core.lowercasing import lowercasing
from .core.punctuation import punctuation_es
from .core.stopwords import stopwords_es
import logging

class Preprocessing:
    """
    Instanciate a preprocessing pipeline for text in spanish.
    Text will be returned vectorized.
    
    :param lowercasing: Lowering the text.
    :type lowercasing: bool
    
    :param DEBUG: Pipeline methods info.
    :type DEBUG: bool
    """
    
    def __init__(self, lowercasing=True, punctuation=True, stopwords=True, debug=False):
        self.lowecasing = lowercasing
        self.debug = debug
        self.punctuation = punctuation
        self.stopwords = stopwords
    
    def pipeline(self, text):
        """
        Preprocesses a given text by
        applying the different preprocessing methods
        
        :param text: The text to be preprocessed
        :type text: str
        
        :return: Preprocessed text
        :rtype: str
        """
        
        if self.debug: logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)8s | %(message)s')
        logging.debug('> Starting preprocessing pipeline...')
        
        # Pipeline creation
        if self.lowecasing: text = lowercasing(text=text, debug=self.debug)
        if self.punctuation: text = punctuation_es(text=text, debug=self.debug)
        if self.stopwords: text = stopwords_es(text=text, debug=self.debug)
        
        logging.debug('Preprocessing pipeline completed! <')
        
        return text
        