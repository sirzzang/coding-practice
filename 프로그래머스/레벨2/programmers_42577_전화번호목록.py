'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10MB)
효율성  테스트
테스트 1 〉	통과 (0.55ms, 10.8MB)
테스트 2 〉	통과 (0.95ms, 11MB)
'''

def solution(phone_book): 
    for i in range(len(phone_book)):
        flag = phone_book[i]
        for v in phone_book[:i] + phone_book[i+1:]:
            if flag in v and v.find(flag) == 0: # 맨 앞에 나오는 경우만
                return False
    return True

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.00ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (1.44ms, 11.1MB)
테스트 2 〉	통과 (1.44ms, 11MB)
'''
def solution(phone_book):
    for i, v in enumerate(phone_book):
        check = phone_book[:i]+phone_book[i+1:] # 나머지 전화번호들
        for number in check:
            if number.find(v) == 0: # 접두사인 경우
                return False
    return True