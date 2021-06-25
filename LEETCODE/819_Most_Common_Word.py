from collections import Counter
import string
from typing import List


def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    # remove punctuation
    for char in paragraph:
        if char in string.punctuation:
            paragraph = paragraph.replace(char, ' ')

    # make lowercase and remove banned word
    to_be_checked = [word for word in paragraph.lower().split()
                     if not word in banned]

    return Counter(to_be_checked).most_common(1)[0][0]


mostCommonWord(
    "Bob hit a ball, the hit BALL flew far after it was hit.", banned=["hit"])
