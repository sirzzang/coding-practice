'''
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer. -> 무슨 소리?
Can you solve the problem in O(1) extra space complexity? -> 고민해 보자.
'''

from typing import List
import math


def productExceptSelf(nums: List[int]) -> List[int]:
    print([math.prod(nums[:i]+nums[i+1:]) for i in range(len(nums))])


productExceptSelf([1, 2, 3, 4])
productExceptSelf([-1, -1, 0, -3, 3])
