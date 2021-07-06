from typing import List


def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    print(sum(nums[i] for i in range(0, len(nums), 2)))


arrayPairSum([6, 2, 6, 5, 1, 2])
