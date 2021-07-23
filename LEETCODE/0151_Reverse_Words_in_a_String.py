'''32ms, 14.5MB'''


def reverseWords(s: str) -> str:
    return " ".join(s.split()[::-1])


reverseWords("the sky is blue")
reverseWords("  hello world  ")
reverseWords("a good    example")
reverseWords("  Bob    Loves  Alice   ")
