from typing import List

# 1. 오답: 99 / 114 test cases passed.
'''
set으로 같은지 판별하면, 문자 개수가 다른 경우 오류가 있다. ex) ["ddddddddddg","dgggggggggg"]
'''


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = {}
    for str_ in strs:
        key = ''.join(sorted(set(str_)))
        if key in anagrams:
            anagrams[key].append(str_)
        else:
            anagrams[key] = [str_]

    return [value for value in anagrams.values()]

# 2.
