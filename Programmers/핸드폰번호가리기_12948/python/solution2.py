import re

def solution(phone_number):
    n = len(phone_number)
    return re.sub("\d", "*", phone_number[:n-4]) + phone_number[n-4:]

'''
정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.2MB)
테스트 2 〉	통과 (0.06ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.1MB)
테스트 4 〉	통과 (0.05ms, 10.2MB)
테스트 5 〉	통과 (0.06ms, 10.2MB)
테스트 6 〉	통과 (0.06ms, 10.2MB)
테스트 7 〉	통과 (0.05ms, 10.2MB)
테스트 8 〉	통과 (0.06ms, 10.1MB)
테스트 9 〉	통과 (0.05ms, 10.3MB)
테스트 10 〉	통과 (0.05ms, 10.2MB)
테스트 11 〉	통과 (0.05ms, 9.98MB)
테스트 12 〉	통과 (0.06ms, 10.2MB)
테스트 13 〉	통과 (0.06ms, 10.3MB)
'''