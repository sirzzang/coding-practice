def longestPalindrome(s:str) -> str:
    l, r = 0, len(s)-1 # pointers
    answer = ''
    while l <= len(s):
        r = len(s)
        while l < r:
            substring = s[l:r]
            if substring == substring[::-1]:
                if len(substring) > len(answer):
                    answer = substring
            r -= 1
        l += 1
    print(answer)
    print('----------------------')
    return answer

longestPalindrome("babad")
longestPalindrome("cbbd")
longestPalindrome("a")
longestPalindrome("ac")
longestPalindrome("abc")
longestPalindrome("bb")
