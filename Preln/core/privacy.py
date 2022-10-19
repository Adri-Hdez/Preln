import logging
import spacy
import re

CLEANDNI = re.compile(
    r"[0-9]{8}[a-z] | [0-9]{8}-[a-z] | [0-9]{2}.[0-9]{3}.[0-9]{3}-[a-z] | [0-9]{2}.[0-9]{3}.[0-9]{3}[a-z] | [a-z][0-9]{7}[a-z] | [a-z][0-9]{7}-[a-z]"
)
CLEANTLFN = re.compile(
    r"((\s\d{9})|(\s\d{3} \d{3} \d{3})|(\s\d{3}-\d{3}-\d{3})|(\s\d{1,3} \d{3}-\d{3}-\d{3})|(\s\+\d{1,3} \d{3} \d{3} \d{3}))"
)
CLEANIP = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")

spanish_nlp = spacy.load("es_core_news_sm")


def privacy(text, format, debug) -> str:
    """
    Method for clean personal data from text.

    :param text: The text to be preprocessed.
    :type: str

    :param format: Type of privacy ([multi | dni | tlfn | name | ip]:[replace | delete]).
    :type: str

    :param debug: Apply debugging
    :type: bool
    """

    if debug:
        logging.basicConfig(
            level=logging.DEBUG, format="%(asctime)s | %(levelname)8s | %(message)s"
        )
    text = text.replace(",", " ,")  # Spacy conflicts with comma

    if "multi" in format:
        if "delete" in format:
            spacy_parser = spanish_nlp(text)
            for entity in spacy_parser.ents:
                if entity.label_ == "PER":
                    text = spacy_parser.text.replace(entity.text, "")
            text = re.sub(CLEANDNI, "", text)
            text = re.sub(CLEANTLFN, "", text)
            text = re.sub(CLEANIP, "", text)
        else:

            text = re.sub(CLEANDNI, " <<DNI>> ", text)
            text = re.sub(CLEANTLFN, " <<TLFN>> ", text)
            text = re.sub(CLEANIP, " <<IP>> ", text)
            spacy_parser = spanish_nlp(text)
            for entity in spacy_parser.ents:
                if entity.label_ == "PER":
                    text = spacy_parser.text.replace(entity.text, "<<PERSON>>")

    if "dni" in format:
        if "delete" in format:
            text = re.sub(CLEANDNI, "", text)
        else:
            text = re.sub(CLEANDNI, " <<DNI>> ", text)
    if "tlfn" in format:
        if "delete" in format:
            text = re.sub(CLEANTLFN, "", text)
        else:
            text = re.sub(CLEANTLFN, " <<TLFN>> ", text)
    if "ip" in format:
        if "delete" in format:
            text = re.sub(CLEANIP, "", text)
        else:
            text = re.sub(CLEANIP, " <<IP>> ", text)
    if "name" in format:
        if "delete" in format:
            spacy_parser = spanish_nlp(text)
            for entity in spacy_parser.ents:
                if entity.label_ == "PER":
                    text = spacy_parser.text.replace(entity.text, "")
        else:
            spacy_parser = spanish_nlp(text)
            for entity in spacy_parser.ents:
                if entity.label_ == "PER":
                    text = spacy_parser.text.replace(entity.text, "<<PERSON>>")

    return text


if __name__ == "__main__":
    privacy()
