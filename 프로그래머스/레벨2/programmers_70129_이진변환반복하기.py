'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.63ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.28ms, 10.1MB)
테스트 10 〉	통과 (1.14ms, 10.3MB)
테스트 11 〉	통과 (0.53ms, 10.3MB)
'''

def binary_change(s):
    # print(s)
    temp = len(s) - s.count('0') # 0을 제거한 후 x의 길이
    c = bin(temp).replace('0b', '') # x를 2진법으로 표현한 문자열
    return c

def solution(s):
    answer = [0, 0] # 이진변환의 횟수, 제거된 0의 개수

    while s != '1':
        answer[1] += s.count('0') # 0 개수 저장
        s = binary_change(s) # 이진변환
        answer[0] += 1 # 이진변환 횟수 업데이트        
    return answer
