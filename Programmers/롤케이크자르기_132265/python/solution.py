from collections import Counter

def solution(topping):
    answer = 0
    
    # 한 사람이 모두 토핑을 가질 경우
    topping_counter = dict(Counter(topping))
    cnt = len(topping_counter)
    
    # 앞에서부터 롤 케이크 잘라 가며 다른 사람에게 토핑 나눠 주기
    split = set()
    for t in topping:
        topping_counter[t] -= 1
        if topping_counter[t] == 0:
            cnt -= 1
        split.add(t)
        
        # 두 사람이 가진 토핑 가짓수가 같은지 체크
        if cnt == len(split):
            answer += 1
        
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (3.35ms, 10.6MB)
테스트 2 〉	통과 (43.24ms, 15.1MB)
테스트 3 〉	통과 (27.94ms, 10.8MB)
테스트 4 〉	통과 (30.26ms, 10.7MB)
테스트 5 〉	통과 (227.44ms, 18.6MB)
테스트 6 〉	통과 (318.65ms, 51.2MB)
테스트 7 〉	통과 (352.82ms, 51.2MB)
테스트 8 〉	통과 (360.89ms, 51.3MB)
테스트 9 〉	통과 (314.93ms, 50.6MB)
테스트 10 〉	통과 (326.02ms, 50.6MB)
테스트 11 〉	통과 (23.10ms, 10.7MB)
테스트 12 〉	통과 (3.48ms, 11.4MB)
테스트 13 〉	통과 (360.00ms, 50.5MB)
테스트 14 〉	통과 (352.85ms, 50.6MB)
테스트 15 〉	통과 (400.16ms, 50.6MB)
테스트 16 〉	통과 (334.94ms, 50.6MB)
테스트 17 〉	통과 (327.22ms, 50.5MB)
테스트 18 〉	통과 (318.11ms, 51.3MB)
테스트 19 〉	통과 (311.26ms, 51.3MB)
테스트 20 〉	통과 (337.44ms, 51.4MB)
'''