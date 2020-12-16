'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
테스트 15 〉	통과 (0.01ms, 10.1MB)
테스트 16 〉	통과 (0.00ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.2MB)
테스트 20 〉	통과 (0.01ms, 10.1MB)
테스트 21 〉	통과 (0.01ms, 10.2MB)
테스트 22 〉	통과 (0.01ms, 10.1MB)
테스트 23 〉	통과 (0.01ms, 10.1MB)
테스트 24 〉	통과 (0.01ms, 10.1MB)
테스트 25 〉	통과 (0.01ms, 10.2MB)
테스트 26 〉	통과 (0.01ms, 10.2MB)
테스트 27 〉	통과 (0.01ms, 10.2MB)
테스트 28 〉	통과 (0.01ms, 10.2MB)
'''
def solution(clothes):
    
    # 의상 종류별 의상 개수 저장
    clothes_dict = {}
    for clothe in clothes:
        c_type = clothe[-1]
        if c_type in clothes_dict:
            clothes_dict[c_type] += 1
        else:
            clothes_dict[c_type] = 1
    
    # 경우의 수
    answer = 1
    for v in clothes_dict.values():
        answer *= (v+1)

    return answer-1