'''시간 초과'''
# def longestPalindrome(s:str) -> str:
#     l, r = 0, len(s)-1 # pointers
#     answer = ''
#     while l <= len(s):
#         r = len(s)
#         while l < r:
#             substring = s[l:r]
#             if substring == substring[::-1]:
#                 if len(substring) > len(answer):
#                     answer = substring
#             r -= 1
#         l += 1
#     print(answer)
#     print('----------------------')
#     return answer


def longestPalindrome(s: str) -> str:
    # 홀수일 때, 짝수일 때
    print()
    left, right = len(s)//2, len(s)//2+1
    while left >= 0 and right < len(s) and s[left:right] == s[left:right][::-1]:
        print(left, right)
        left -= 1
        right += 1
    print(left, right, s[left:right])


longestPalindrome("babad")
longestPalindrome("cbbd")
longestPalindrome("a")
longestPalindrome("ac")
longestPalindrome("abc")
longestPalindrome("bb")
