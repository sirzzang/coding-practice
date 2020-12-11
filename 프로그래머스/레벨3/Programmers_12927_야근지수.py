'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.18ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.53ms, 10.2MB)
테스트 9 〉	통과 (0.82ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.1MB)
테스트 13 〉	통과 (0.00ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (356.69ms, 10.2MB)
테스트 2 〉	통과 (429.44ms, 10.2MB)
'''

import heapq

def solution(n, works):
    if n >= sum(works):
        return 0
    
    works_heap = []
    for work in works:
        heapq.heappush(works_heap, -work)
    
    while n:
        max_work = heapq.heappop(works_heap)
        max_work += 1
        n -= 1
        heapq.heappush(works_heap, max_work)
        # print("남은 시간:", n, "남은 작업량:", works_heap)
            
    answer = 0
    for work in works_heap:
        answer += (work**2)
        
    return answer