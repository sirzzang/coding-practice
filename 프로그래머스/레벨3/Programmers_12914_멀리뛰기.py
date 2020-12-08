'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.07ms, 10.2MB)
테스트 8 〉	통과 (0.06ms, 10.2MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
테스트 10 〉	통과 (0.04ms, 10.2MB)
테스트 11 〉	통과 (0.35ms, 10.2MB)
테스트 12 〉	통과 (0.32ms, 10.2MB)
테스트 13 〉	통과 (0.20ms, 10.2MB)
테스트 14 〉	통과 (0.41ms, 10.2MB)
테스트 15 〉	통과 (0.26ms, 10.2MB)
테스트 16 〉	통과 (0.35ms, 10.2MB)
'''
def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b, answer = 1, 2, 0
        for i in range(3, n+1):
            answer = (a%1234567 +b%1234567)%1234567
            a = b
            b = answer
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.1MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.12ms, 10.2MB)
테스트 8 〉	통과 (0.09ms, 10.2MB)
테스트 9 〉	통과 (0.08ms, 10.2MB)
테스트 10 〉	통과 (0.06ms, 10.2MB)
테스트 11 〉	통과 (0.66ms, 10.2MB)
테스트 12 〉	통과 (0.71ms, 10.2MB)
테스트 13 〉	통과 (0.36ms, 10.2MB)
테스트 14 〉	통과 (0.85ms, 10.3MB)
테스트 15 〉	통과 (0.53ms, 10.2MB)
테스트 16 〉	통과 (0.63ms, 10.2MB)
'''
def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        answer = [0] * n
        answer[0], answer[1] = 1, 2
        for i in range(2, n):
            answer[i] = (answer[i-1]%1234567 + answer[i-2]%1234567)%1234567
        return answer[-1]
