import logging

from symspellpy.symspellpy import SymSpell
from pathlib import Path

def autocorrect(text, debug):
    """
    Method for auto-correct words in text.

    :param text: The text to be preprocessed.
    :type: str

    :param debug: Apply debugging
    :type: bool
    """

    if debug:
        logging.basicConfig(
            level=logging.DEBUG, format="%(asctime)s | %(levelname)8s | %(message)s"
        )

    path = Path(__file__).parent.parent / "./_external/dict/es-100l.txt"

    sym_spell = SymSpell()

    sym_spell.load_dictionary(path,0,1)

    suggestion = sym_spell.word_segmentation(text)
    return suggestion.corrected_string



if __name__ == "__main__":
    corregido = autocorrect("holaquétal",False)
    print(corregido)