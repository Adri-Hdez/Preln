import logging
import re

def numbers_cleanner(text, debug):
    """
    Method for delete numbers.
    
    :param text: The text to be preprocessed
    :type: str
    
    :param debug: Apply debugging
    :type: bool
    """
    
    if debug: logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)8s | %(message)s')
    
    text = re.sub('\d', '', text)
    logging.debug('-- Numbers deleted!')
    return text


if __name__ == '__main__':
  numbers_cleanner()