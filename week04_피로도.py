# 완전탐색: 필요 없는 함수 및 예외 체크 조건 제거
'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.04ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.43ms, 10.2MB)
테스트 6 〉	통과 (3.09ms, 10.2MB)
테스트 7 〉	통과 (26.50ms, 10.3MB)
테스트 8 〉	통과 (28.34ms, 10.2MB)
테스트 9 〉	통과 (0.08ms, 10.2MB)
테스트 10 〉	통과 (2.62ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.4MB)
테스트 12 〉	통과 (15.68ms, 10.2MB)
테스트 13 〉	통과 (12.30ms, 10.2MB)
테스트 14 〉	통과 (12.20ms, 10.2MB)
테스트 15 〉	통과 (10.58ms, 10.3MB)
테스트 16 〉	통과 (1.24ms, 10.3MB)
테스트 17 〉	통과 (10.99ms, 10.2MB)
'''
from itertools import permutations

def solution(k, dungeons):    
    answer = 0
    for perm in permutations(dungeons):
        curr, cnt = k, 0
        for dungeon in perm:
            if dungeon[0] <= curr:
                curr -= dungeon[1]
                cnt += 1
            else:
                break
        if cnt > answer:
            answer = cnt

    return answer

# 완전탐색: 최악의 경우 8!x8
'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.06ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.4MB)
테스트 5 〉	통과 (0.47ms, 10.3MB)
테스트 6 〉	통과 (3.46ms, 10.3MB)
테스트 7 〉	통과 (43.86ms, 10.2MB)
테스트 8 〉	통과 (33.30ms, 10.2MB)
테스트 9 〉	통과 (0.06ms, 10.3MB)
테스트 10 〉	통과 (3.76ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.2MB)
테스트 12 〉	통과 (32.08ms, 10.3MB)
테스트 13 〉	통과 (27.65ms, 10.3MB)
테스트 14 〉	통과 (24.36ms, 10.2MB)
테스트 15 〉	통과 (22.05ms, 10.2MB)
테스트 16 〉	통과 (2.51ms, 10.2MB)
테스트 17 〉	통과 (24.94ms, 10.2MB)
'''
from functools import reduce
from itertools import permutations

def explore(k, dungeons):
    count = 0
    for dungeon in dungeons:
        required, consumed = dungeon
        # 최소 필요도 조건을 충족하지 않는 경우
        if required > k:
            continue
            
        # 남아 있는 피로도가 없을 경우
        if k <= 0:
            return count
        count += 1
        k -= consumed
    
    return count

def solution(k, dungeons):
    # 전체 다 탐험할 수 있는 경우
    max_k = reduce(lambda acc, cur: acc + cur[1], dungeons, 0)
    if max_k <= k:
        return len(dungeons)
    
    answer = 0
    for perm in permutations(dungeons):
        count = explore(k, perm)
        if count > answer:
            answer = count
    return answer

# 틀린 풀이: 소모 피로도가 낮은 걸 먼저 가버리면 최소 필요 피로도를 고려하지 못하게 됨
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	실패 (0.01ms, 10.2MB)
테스트 12 〉	실패 (0.02ms, 10.3MB)
테스트 13 〉	실패 (0.01ms, 10.3MB)
테스트 14 〉	실패 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	실패 (0.01ms, 10.3MB)
'''
from functools import reduce

def solution(k, dungeons):
    # 전체 다 탐험할 수 있는 경우
    max_k = reduce(lambda acc, cur: acc + cur[1], dungeons, 0)
    if max_k <= k:
        return len(dungeons)
    
    answer = 0
    while k and dungeons:
        # 탐험을 위해 필요한 최소 피로도가 현재 피로도 이하인 던전 
        candidates = [dungeon for dungeon in dungeons if dungeon[0] <= k]
        if not candidates:
            return answer
        
        candidates.sort(key=lambda x: x[1])
        visited = candidates[0]
        k -= visited[1]
        answer += 1
        dungeons.remove(visited)        
    
    return answer