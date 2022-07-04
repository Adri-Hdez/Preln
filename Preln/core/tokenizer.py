import logging
import nltk
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
    
from nltk.tokenize import word_tokenize

def tokenizer(text, debug):
    """
    Method for tokenize text.
    
    :param text: The text to be preprocessed
    :type: str
    
    :param debug: Apply debugging
    :type: bool
    """
    
    if debug: logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)8s | %(message)s')
    
    text = word_tokenize(text)
    logging.debug('-- text tokenized!')

    return text


if __name__ == '__main__':
    tokenizer()