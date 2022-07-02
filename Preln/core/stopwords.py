import pandas as pd
import logging
from pathlib import Path
import csv

path = Path(__file__).parent / "../_external/stopwords.csv"
stopwords = pd.read_csv(path)['stopwords'].tolist()

def stopwords_es(text, debug):
    """
    Method for eliminate text punctuation.
    
    :param text: The text to be preprocessed
    :type: str
    
    :param debug: Apply debugging
    :type: bool
    """
    
    if debug: logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)8s | %(message)s')
    
    text = text.split()    
    text = " ".join(word for word in text if word not in stopwords)
    logging.debug('-- Stopwords cleanned!')
    
    return text


if __name__ == '__main__':
  stopwords_es()