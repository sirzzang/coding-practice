'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.05ms, 10.2MB)
테스트 3 〉	통과 (0.80ms, 10.3MB)
테스트 4 〉	통과 (0.87ms, 10.3MB)
테스트 5 〉	통과 (1.23ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.50ms, 10.3MB)
테스트 8 〉	통과 (0.57ms, 10.4MB)
테스트 9 〉	통과 (0.03ms, 10.2MB)
테스트 10 〉	통과 (1.13ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (186.09ms, 18.8MB)
테스트 2 〉	통과 (129.98ms, 17.7MB)
테스트 3 〉	통과 (232.28ms, 19.5MB)
테스트 4 〉	통과 (165.47ms, 18.2MB)
테스트 5 〉	통과 (110.55ms, 17MB)
'''

def solution(prices):
    answer = [0]*len(prices)    

    for i in range(len(prices)):
        # 현재 주식 가격
        curr = prices[i]

        # 떨어진 날이 있는지 검사
        for j in range(i+1, len(prices)):
            if prices[j] < curr:
                answer[i] = j-i
                break
            answer[i] = len(prices)-i-1
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.20ms, 10.3MB)
테스트 4 〉	통과 (0.24ms, 10.3MB)
테스트 5 〉	통과 (0.27ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.15ms, 10.3MB)
테스트 8 〉	통과 (0.18ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.27ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (24.53ms, 18.8MB)
테스트 2 〉	통과 (18.13ms, 17.4MB)
테스트 3 〉	통과 (24.81ms, 19.5MB)
테스트 4 〉	통과 (20.96ms, 18.4MB)
테스트 5 〉	통과 (15.21ms, 17MB)
'''

def solution(prices):
    answer = [0]*len(prices)
    stack = []
    
    for i in range(len(prices)):
        if not stack:
            stack.append(i)
        else:
        # 스택 top 시간의 주식 가격이 현재 주식 가격보다 크면,
        # 주식 가격이 유지되지 않은 것
            while stack and prices[stack[-1]] > prices[i]:
                top = stack.pop()
                answer[top] = i - top
            stack.append(i)
    
    # 마지막까지 떨어지지 않은 주식 가격
    while stack:
        top = stack.pop()
        answer[top] = len(prices) - top - 1
    return answer