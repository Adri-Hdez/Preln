import logging
import string

def punctuation_es(text, debug):
    """
    Method for eliminate text punctuation.
    
    :param text: The text to be preprocessed
    :type: str
    
    :param debug: Apply debugging
    :type: bool
    """
    
    if debug: logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)8s | %(message)s')
    
    punctuation_words = string.punctuation + '¿¡·' 
    text = "".join(word for word in text if word not in punctuation_words)
    logging.debug('-- Punctuation cleanned!')

    return text


if __name__ == '__main__':
  punctuation_es()