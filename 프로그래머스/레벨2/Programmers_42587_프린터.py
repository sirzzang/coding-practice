'''
정확성  테스트
테스트 1 〉	통과 (0.71ms, 10.2MB)
테스트 2 〉	통과 (5.41ms, 10.1MB)
테스트 3 〉	통과 (0.28ms, 10.2MB)
테스트 4 〉	통과 (0.13ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.51ms, 10.2MB)
테스트 7 〉	통과 (0.53ms, 10.2MB)
테스트 8 〉	통과 (3.76ms, 10.2MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
테스트 10 〉	통과 (0.54ms, 10.2MB)
테스트 11 〉	통과 (1.68ms, 10.2MB)
테스트 12 〉	통과 (0.12ms, 10.2MB)
테스트 13 〉	통과 (2.02ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.04ms, 10.3MB)
테스트 16 〉	통과 (0.15ms, 10.2MB)
테스트 17 〉	통과 (3.91ms, 10.1MB)
테스트 18 〉	통과 (0.04ms, 10.3MB)
테스트 19 〉	통과 (1.91ms, 10.3MB)
테스트 20 〉	통과 (0.41ms, 10.2MB)
'''

from collections import deque

def solution(priorities, location):
    if len(priorities) == 1:
        return 1
    priorities = deque([(i, v) for i, v in enumerate(priorities)]) # 위치 기억해야 하므로 index 저장
    answer = 0
    while priorities:
        cur = priorities[0]
        if cur[1] >= max(priorities, key=lambda x:x[1])[1]: 
            # print(f"{cur} 인쇄")
            answer += 1
            if priorities.popleft()[0] == location:
                return answer
        else:
            priorities.popleft()
            priorities.append(cur)  
    # return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.41ms, 10.2MB)
테스트 2 〉	통과 (1.11ms, 10.2MB)
테스트 3 〉	통과 (0.06ms, 10.2MB)
테스트 4 〉	통과 (0.04ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.16ms, 10.2MB)
테스트 7 〉	통과 (0.15ms, 10.1MB)
테스트 8 〉	통과 (0.85ms, 10.3MB)
테스트 9 〉	통과 (0.04ms, 10.2MB)
테스트 10 〉	통과 (0.19ms, 10.2MB)
테스트 11 〉	통과 (0.99ms, 10.1MB)
테스트 12 〉	통과 (0.04ms, 10.2MB)
테스트 13 〉	통과 (0.59ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.02ms, 10.2MB)
테스트 16 〉	통과 (0.08ms, 10.2MB)
테스트 17 〉	통과 (0.78ms, 10.2MB)
테스트 18 〉	통과 (0.03ms, 10.2MB)
테스트 19 〉	통과 (0.71ms, 10.1MB)
테스트 20 〉	통과 (0.09ms, 10.2MB)
'''

def solution(papers, location):
    
    if len(papers) == 1:
        return 1
    
    front = 0 # top의 위치
    back = len(papers)-1 # back의 위치
    pop_idx = None # pop할 때의 index : if 조건이 만족되지 않을 때 top을 pop한다.
    flag_idx = location # 문제에서 찾으라고 한 기준 index
    cnt = 0 # pop한 횟수 = 인쇄 횟수

    while pop_idx != flag_idx:
        if any(paper > papers[front] for paper in papers[front+1:]): # front 뒤에 애가 하나라도 크다면
            papers.append(papers[front]) # top을 뒤로 보냄.
            front += 1
            back += 1
            if front - 1 == flag_idx: # 찾아야 할 flag가 top에 있었고, 뒤로 밀렸다면,
                flag_idx = back # flag의 index도 변함.
        else: # front 뒤에 큰 애가 없다 = 인쇄한다면,
            pop_idx = front # top을 pop
            front += 1 # front의 위치만 +1
            cnt += 1
    
    return cnt