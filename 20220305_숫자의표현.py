'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (0.06ms, 10.1MB)
테스트 2 〉	통과 (0.03ms, 10.1MB)
테스트 3 〉	통과 (0.05ms, 10.3MB)
테스트 4 〉	통과 (0.04ms, 10.1MB)
테스트 5 〉	통과 (0.06ms, 10.1MB)
테스트 6 〉	통과 (0.06ms, 10.1MB)
'''

def divide_even(num, d):
    return 1 if num % d == d // 2 else 0

def divide_odd(num, d):
    return 1 if num % d == 0 else 0

def solution(n):
    # 자기 자신은 반드시 포함
    answer = 1
    
    for i in range(2, n):
        # i개로 표현할 수 있는 합의 최솟값 제약
        if i * (i + 1) / 2 > n:
            break

        if i % 2 == 0:
            answer += divide_even(n, i)
        else:
            answer += divide_odd(n, i)
    
    return answer