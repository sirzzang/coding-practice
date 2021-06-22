import re

'''
class Solution:

    def isPalindrome(self, s:str) -> bool:
        to_be_checked = [char.lower() for char in s if char.isalnum()]
        return to_be_checked == to_be_checked[::-1] 
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        to_be_checked = ''.join([char.lower() for char in s if char.isalnum()])
        if len(to_be_checked) <= 1:
            return True

        for i in range(0, len(to_be_checked)//2):
            if to_be_checked[i] != to_be_checked[-i-1]:
                return False
        return True


Solution().isPalindrome("0z;z   ; 0")
