from typing import List

# 1. [3, 2, 3], 6의 경우 3이 2개 있어서 안 된다
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         answer = []
#         for i, v in enumerate(nums):
#             if i != nums.index(target-v):
#                 answer.append(i)
#                 answer.append(nums.index(target-v))
#                 break
#         return answer


# 2. 인덱스 유지하기 위해 원래 자리에 더미 원소 추가: 비효율적
# def twoSum(nums: List[int], target: int) -> List[int]:
#     for i, v in enumerate(nums):
#         temp = nums[:i] + [''] + nums[i+1:]  # 인덱스 유지
#         if target - v in temp:
#             return [i, temp.index(target-v)]

def twoSum(nums: List[int], target: int) -> List[int]:
    print()
    for i, v in enumerate(nums):
        if v > target:
            continue
        if target - v in nums:
            print(i, v, nums.index(target-v))

twoSum([3, 2, 4], 6)
twoSum([2, 7, 11, 15], 9)
twoSum([3, 3], 6)
