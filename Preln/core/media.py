import logging
import re

CLEANHTML = re.compile("<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});")
CLEANURL = re.compile(r"http\S+")
CLEANMENTIONS = re.compile("@([a-zA-Z0-9_]{1,50})")
CLEANHASHTAGS = re.compile("#([a-zA-Z0-9_]{1,50})")
CLEANEMAIL = re.compile(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+")


def media(text, format, debug) -> str:
    """
    Method for delete social media tags in text.

    :param text: The text to be preprocessed.
    :type: str

    :param format: Type of social media ([multi | html | url | mention | hashtag | email]:[replace | delete]).
    :type: str

    :param debug: Apply debugging
    :type: bool
    """

    if debug:
        logging.basicConfig(
            level=logging.DEBUG, format="%(asctime)s | %(levelname)8s | %(message)s"
        )

    if "multi" in format:
        if "delete" in format:
            text = re.sub(CLEANHTML, "", text)
            text = re.sub(CLEANURL, "", text)
            text = re.sub(CLEANEMAIL, "", text)
            text = re.sub(CLEANHASHTAGS, "", text)
            text = re.sub(CLEANMENTIONS, "", text)
        else:
            text = re.sub(CLEANHTML, "", text)  # Waiting for issues..
            text = re.sub(CLEANURL, "<<URL>>", text)
            text = re.sub(CLEANEMAIL, "<<EMAIL>>", text)
            text = re.sub(CLEANHASHTAGS, "<<HASHTAG>>", text)
            text = re.sub(CLEANMENTIONS, "<<MENTION>>", text)
    if "html" in format:
        if "delete" in format:
            text = re.sub(CLEANHTML, "", text)
        else:
            text = re.sub(CLEANHTML, " <<HTMLTAG>> ", text)
    if "hashtag" in format:
        if "delete" in format:
            text = re.sub(CLEANHASHTAGS, "", text)
        else:
            text = re.sub(CLEANHASHTAGS, "<<HASHTAG>>", text)
    if "url" in format:
        if "delete" in format:
            text = re.sub(CLEANURL, "", text)
        else:
            text = re.sub(CLEANURL, "<<URL>>", text)
    if "mention" in format:
        if "delete" in format:
            text = re.sub(CLEANMENTIONS, "", text)
        else:
            text = re.sub(CLEANMENTIONS, "<<MENTION>>", text)
    if "email" in format:
        if "delete" in format:
            text = re.sub(CLEANEMAIL, "", text)
        else:
            text = re.sub(CLEANEMAIL, "<<EMAIL>>", text)

    return text


if __name__ == "__main__":
    media()
