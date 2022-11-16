from collections import deque

def solution(ingredient):
    answer = 0
    
    d = deque(ingredient)
    stack = []
    burger = [1, 2, 3, 1]
    while d:
        stack.append(d.popleft())
        if len(stack) >= 4 and stack[-4:] == burger:
            answer += 1
            stack = stack[:-4]
        # print(f"ingredient: {d}, stack: {stack}, answer: {answer}")    
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (1397.63ms, 19MB)
테스트 4 〉	통과 (6490.59ms, 30.1MB)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	통과 (3152.47ms, 24.2MB)
테스트 7 〉	통과 (5350.17ms, 27.8MB)
테스트 8 〉	통과 (3528.09ms, 24.7MB)
테스트 9 〉	통과 (1986.48ms, 21.2MB)
테스트 10 〉	통과 (2.91ms, 10.3MB)
테스트 11 〉	통과 (989.66ms, 17.8MB)
테스트 12 〉	실패 (시간 초과)
테스트 13 〉	통과 (0.00ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 9.96MB)
테스트 15 〉	통과 (0.00ms, 10.1MB)
테스트 16 〉	통과 (0.00ms, 10.1MB)
테스트 17 〉	통과 (0.00ms, 10.1MB)
'''