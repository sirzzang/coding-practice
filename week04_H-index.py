'''
정확성  테스트
테스트 1 〉	통과 (0.46ms, 10.2MB)
테스트 2 〉	통과 (1.87ms, 10.2MB)
테스트 3 〉	통과 (0.88ms, 10.2MB)
테스트 4 〉	통과 (0.77ms, 10.2MB)
테스트 5 〉	통과 (1.45ms, 10.2MB)
테스트 6 〉	통과 (1.97ms, 10.2MB)
테스트 7 〉	통과 (0.13ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.24ms, 10.2MB)
테스트 11 〉	통과 (2.57ms, 10.4MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (1.53ms, 10.2MB)
테스트 14 〉	통과 (1.17ms, 10.2MB)
테스트 15 〉	통과 (1.86ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
'''

def solution(citations):
    # 최대 h에서부터 탐색 시작
    h = len(citations)
    while h:
        # citations 배열 중 h회 이상 인용된 논문의 수
        cur_h = len([c for c in citations if c >= h])
        
        # h회 이상 인용된 논문의 수가 h편 이상이면
        if cur_h >= h:
            print('here', cur_h, h)
            return h
        
        h -= 1
    
    return h