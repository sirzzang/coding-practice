from collections import deque

def solution(ingredient):
    answer = 0
    
    d = deque(ingredient)
    stack = ""
    burger = "1231"
    while d:
        stack += str(d.popleft())
        if len(stack) >= 4 and stack[-4:] == burger:
            answer += 1
            stack = stack[:-4]
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (120.59ms, 14.7MB)
테스트 4 〉	통과 (325.03ms, 20MB)
테스트 5 〉	통과 (550.01ms, 23MB)
테스트 6 〉	통과 (224.32ms, 17.1MB)
테스트 7 〉	통과 (303.34ms, 19.2MB)
테스트 8 〉	통과 (225.85ms, 17.6MB)
테스트 9 〉	통과 (157.58ms, 15.7MB)
테스트 10 〉	통과 (3.38ms, 10.2MB)
테스트 11 〉	통과 (115.37ms, 14MB)
테스트 12 〉	통과 (682.41ms, 25.7MB)
테스트 13 〉	통과 (0.00ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.00ms, 10.1MB)
테스트 17 〉	통과 (0.00ms, 10.1MB)
'''