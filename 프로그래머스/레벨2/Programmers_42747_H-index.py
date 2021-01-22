'''
정확성  테스트
테스트 1 〉	통과 (0.09ms, 10.3MB)
테스트 2 〉	통과 (0.16ms, 10.3MB)
테스트 3 〉	통과 (0.16ms, 10.3MB)
테스트 4 〉	통과 (0.13ms, 10.2MB)
테스트 5 〉	통과 (0.16ms, 10.2MB)
테스트 6 〉	통과 (0.19ms, 10.2MB)
테스트 7 〉	통과 (0.06ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.1MB)
테스트 10 〉	통과 (0.08ms, 10.2MB)
테스트 11 〉	통과 (0.20ms, 10.3MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.18ms, 10.3MB)
테스트 14 〉	통과 (0.17ms, 10.2MB)
테스트 15 〉	통과 (0.18ms, 10.3MB)
테스트 16 〉	통과 (0.00ms, 10.2MB)
'''
def solution(citations):
    citations.sort(reverse=True) # 인용횟수 많은 순으로 정렬

    h = -1
    for i, v in enumerate(citations): # O(1000)
        # i번째에서 인용된 논문의 수(i+1)가 인용 횟수(v)보다 많을 때 순회 중단
        if i+1 >= v:
            h = v
            cnt = i+1 # h회 이상 인용된 논문의 수
            break
    
    if h == -1: # 모든 논문의 인용횟수가 발표한 논문 수보다 많은 경우
        return len(citations)
    
    if h < cnt: # 예외 처리
        return cnt-1
    return h