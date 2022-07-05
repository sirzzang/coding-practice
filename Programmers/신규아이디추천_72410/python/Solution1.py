import re

def solution(new_id):
    answer = new_id.lower() # 1단계
    answer = re.sub("[^a-z0-9-_.]", "", answer) # 2단계
    answer = re.sub("[.]{2,}", ".", answer) # 3단계
    answer = answer.strip(".") # 4단계
    if not answer: # 5단계
        answer = "a"
    if len(answer) >= 16: # 6단계
        answer = answer[:15].rstrip(".")
    if len(answer) <= 2: # 7단계
        answer += answer[-1] * (3 - len(answer))    
    
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.15ms, 10.4MB)
테스트 2 〉	통과 (0.14ms, 10.2MB)
테스트 3 〉	통과 (0.15ms, 10.5MB)
테스트 4 〉	통과 (0.15ms, 10.3MB)
테스트 5 〉	통과 (0.15ms, 10.4MB)
테스트 6 〉	통과 (0.14ms, 10.5MB)
테스트 7 〉	통과 (0.15ms, 10.3MB)
테스트 8 〉	통과 (0.14ms, 10.3MB)
테스트 9 〉	통과 (0.21ms, 10.3MB)
테스트 10 〉	통과 (0.15ms, 10.4MB)
테스트 11 〉	통과 (0.14ms, 10.2MB)
테스트 12 〉	통과 (0.15ms, 10.3MB)
테스트 13 〉	통과 (0.16ms, 10.4MB)
테스트 14 〉	통과 (0.14ms, 10.4MB)
테스트 15 〉	통과 (0.15ms, 10.4MB)
테스트 16 〉	통과 (0.15ms, 10.3MB)
테스트 17 〉	통과 (0.16ms, 10.3MB)
테스트 18 〉	통과 (0.28ms, 10.3MB)
테스트 19 〉	통과 (0.20ms, 10.5MB)
테스트 20 〉	통과 (0.24ms, 10.4MB)
테스트 21 〉	통과 (0.27ms, 10.3MB)
테스트 22 〉	통과 (0.24ms, 10.5MB)
테스트 23 〉	통과 (0.22ms, 10.3MB)
테스트 24 〉	통과 (0.16ms, 10.4MB)
테스트 25 〉	통과 (0.18ms, 10.2MB)
테스트 26 〉	통과 (0.15ms, 10.3MB)
'''