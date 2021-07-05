from typing import List

'''이거 옛날에 백트래킹할 때 순열 조합 구하는 거랑 비슷했던 것 같은데'''

# 브루트포스: 시간 초과


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        answer = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        zero_sum = sorted([nums[i], nums[j], nums[k]])
                        if zero_sum not in answer:
                            answer.append(zero_sum)
        return answer
