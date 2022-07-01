import logging

def accents(text, debug):
    """
    Method for delete accents.
    
    :param text: The text to be preprocessed
    :type: str
    
    :param debug: Apply debugging
    :type: bool
    """
    
    if debug: logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)8s | %(message)s')
    
    dictionary = {'á': 'a', 'à': 'a', 'â': 'a', 'ä': 'a', 
                  'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
                  'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
                  'ó': 'o', 'ò': 'o', 'ô': 'o', 'ö': 'o',
                  'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
                  
                  'Á': 'A', 'À': 'A', 'Â': 'A', 'Ä': 'A', 
                  'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E',
                  'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
                  'Ó': 'O', 'Ò': 'O', 'Ô': 'O', 'Ö': 'O',
                  'Ú': 'U', 'Ù': 'U', 'Û': 'U', 'Ü': 'U'}
    
    for accent, no_accent in dictionary.items():
        text = text.replace(accent, no_accent)
    logging.debug('-- Accent cleanned!')

    return text


if __name__ == '__main__':
    accents()