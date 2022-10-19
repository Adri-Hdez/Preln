from .__features.lev_distance import correction
import logging


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

    text = text.split()
    texts = []

    for word in text:
        word_corrected = correction(word)
        texts.append(word_corrected)

    texts = " ".join(texts)
    logging.debug("-- Text corrected!")

    return texts


if __name__ == "__main__":
    autocorrect()
