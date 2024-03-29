from collections import Counter
from pathlib import Path
import re


def words(text):
    return re.findall(r"\w+", text.lower())


path = Path(__file__).parent.parent.parent / "./_external/corpus.txt"
WORDS = Counter(words(open(path, encoding="utf8").read()))


def PROB(word, N=sum(WORDS.values())):
    "Probability of `word`."
    return WORDS[word] / N


def correction(word):
    "Most probable spelling correction for word."
    return max(candidates(word), key=PROB)


def candidates(word):
    "Generate possible spelling corrections for word."
    return (
        known([word]) or known(first_edit(word)) or known(second_edit(word)) or [word]
    )


def known(words):
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)


def first_edit(word):
    "All edits that are one edit away from `word`."
    letters = "abcdefghijklmnopqrstuvwxyz"
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def second_edit(word):
    "All edits that are two edits away from `word`."
    return (e2 for e1 in first_edit(word) for e2 in first_edit(e1))
