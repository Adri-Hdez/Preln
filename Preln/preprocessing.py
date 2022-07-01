from .core.lowercasing import lowercasing
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
    
    def __init__(self, lowercasing=True, debug=False):
        self.lowecasing = lowercasing
        self.debug = debug
    
    def pipeline(self, text):
        """
        Preprocesses a given text by
        applying the different preprocessing methods
        
        :param text: The text to be preprocessed
        :type text: str
        
        :return: Preprocessed text
        :rtype: str
        """
        
        if self.debug: logging.basicConfig(level=logging.DEBUG)
        logging.debug('> Starting preprocessing pipeline...')
        
        # Pipeline creation
        if self.lowecasing: text = lowercasing(text=text, debug=self.debug)
        
        return text
        