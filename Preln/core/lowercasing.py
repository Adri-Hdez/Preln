import logging

def lowercasing(text, debug):
    """
    Method for lowercase text.
    
    :param text: The text to be preprocessed
    :type: str
    
    :param debug: Apply debugging
    :type: bool
    """
    
    if debug: logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)8s | %(message)s')
    
    text = "".join(word.lower() for word in text)
    logging.debug('-- The text is in lowercase!')
    return text


if __name__ == '__main__':
  lowercasing()