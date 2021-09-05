from typing import List

'''이거 옛날에 백트래킹할 때 순열 조합 구하는 거랑 비슷했던 것 같은데'''

# 브루트포스: 시간 초과
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         if len(nums) < 3:
#             return []

#         answer = []
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 for k in range(j+1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         zero_sum = sorted([nums[i], nums[j], nums[k]])
#                         if zero_sum not in answer:
#                             answer.append(zero_sum)
#         return answer

def threeSum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []

    answer = []

    nums.sort()
    left, right = 0, len(nums) - 1
    while left <= right:
        left_value, right_value = nums[left], nums[right]
        if -(left_value + right_value) in nums[left+1:right]:
            answer.append([left_value, -(left_value+right_value), right_value])
        if left_value + right_value <= 0:
            left += 1
        elif left_value + right_value > 0:
            right -= 1
    print(answer)

threeSum([-1, 0, 1, 2, -1, -4])
threeSum([0, 0, 0])