from typing import List

'''260ms, 16.9MB'''


def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    return sum(nums[i] for i in range(0, len(nums), 2))


arrayPairSum([6, 2, 6, 5, 1, 2])
