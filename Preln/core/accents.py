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
    
    dictionary = {'a': ['á', 'à', 'â', 'ä'],  
                  'e': ['é', 'è', 'ê', 'ë'],  
                  'i': ['í', 'ì', 'î', 'ï'],  
                  'o': ['ó', 'ò', 'ô', 'ö'],  
                  'u': ['ú', 'ù', 'û', 'ü'],  
                  
                  'A': ['Á', 'À', 'Â', 'Ä'],  
                  'E': ['É', 'È', 'Ê', 'Ë'],  
                  'I': ['Í', 'Ì', 'Î', 'Ï'],  
                  'O': ['Ó', 'Ò', 'Ô', 'Ö'],  
                  'U': ['Ú', 'Ù', 'Û', 'Ü']}  

    for no_accent, accent in dictionary.items():
        for type in accent:
            text = text.replace(type, no_accent)
    logging.debug('-- Accent cleanned!')

    return text


if __name__ == '__main__':
    accents()