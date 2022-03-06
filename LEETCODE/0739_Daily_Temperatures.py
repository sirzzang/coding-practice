from typing import List
'''비슷한 문제: 프로그래머스 주식가격'''

# O(n^2) 풀이
'''
TimeLimitExceeded:
[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,...]
'''
# def dailyTemperatures(temperatures: List[int]) -> List[int]:
#     if len(temperatures) == 1:
#         return [0]

#     answer = [0] * len(temperatures)
#     for i in range(len(temperatures)):
#         cur = temperatures[i]
#         for j in range(i+1, len(temperatures)):
#             if temperatures[j] > cur:
#                 answer[i] = j-i
#                 break            
#         print(cur, answer)
#     print()

# 1232ms, 25.5MB
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    print()
    if len(temperatures) == 1:
        return [0]

    stack = []
    answer = [0] * len(temperatures)
    for i, temp in enumerate(temperatures):
        while stack and temp > stack[-1][1]:
            top = stack.pop()
            answer[top[0]] = i - top[0]
        stack.append((i, temp))
        print(i, temp, stack)
    print(answer)



dailyTemperatures([73,74,75,71,69,72,76,73])
dailyTemperatures([30,40,50,60])
dailyTemperatures([30,60,90])
