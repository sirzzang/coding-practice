# O(n^2) 풀이: 388ms, 14.4MB
def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0

    answer = 0
    for i in range(len(s)):
        temp = s[i]
        for j in range(i+1, len(s)):
            if s[j] in temp:
                break
            temp += s[j]
        if len(temp) > answer:
            answer = len(temp)
    print(answer)


lengthOfLongestSubstring("abcabcbb")
lengthOfLongestSubstring("bbbbb")
lengthOfLongestSubstring("pwwkew")
