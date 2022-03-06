# O(n^2) 풀이
'''
정확성  테스트
테스트 1 〉	통과 (158.96ms, 50MB)
테스트 2 〉	통과 (169.27ms, 49.5MB)
테스트 3 〉	통과 (0.16ms, 10.2MB)
테스트 4 〉	통과 (0.56ms, 10.3MB)
테스트 5 〉	통과 (4.66ms, 11.2MB)
테스트 6 〉	통과 (0.30ms, 10.2MB)
테스트 7 〉	통과 (0.27ms, 10.1MB)
테스트 8 〉	통과 (1.26ms, 10.4MB)
'''
def solution(numbers, target):
    sum_list = [0]
    for number in numbers:
        current_sum = []
        # 직전까지 순회한 number로 만들 수 있는 합에 현재 number를 더하고 뺀 값 기록
        for prev_sum in sum_list:
            current_sum.append(prev_sum + number)
            current_sum.append(prev_sum - number)
        
        # 합 리스트 교체
        sum_list = current_sum
    return sum_list.count(target)

# 다른 풀이: DFS
def dfs(nums, i, n, t):
    ret = 0
    if i==len(nums):
        if n==t: return 1
        else: return 0
    ret += dfs(nums, i+1, n+nums[i], t)
    ret += dfs(nums, i+1, n-nums[i], t)
    return ret

def solution(numbers, target):
    answer = dfs(numbers, 0, 0, target)
    return answer

# 다른 풀이
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

# 다른 풀이
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))