# 1. 360ms, 15.1MB
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums_str = ''.join([str(n) for n in nums]).split('0')
        return len(max(nums_str, key=len))

# 2. 348ms, 14.2MB


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        answer = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                max_ones += 1
            else:
                if max_ones > answer:
                    answer = max_ones
                max_ones = 0

        return answer if max_ones <= answer else max_ones

# 3. 340ms, 14.4MB


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        answer = 0
        for num in nums:
            if num == 1:
                max_ones += 1
            else:  # 0인 경우
                answer = max(max_ones, answer)
                if answer >= len(nums)/2:  # 이미 0이 나온 위치가 가운데 이상인 경우
                    return answer
                max_ones = 0
        return max(max_ones, answer)
