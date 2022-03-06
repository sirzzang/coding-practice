# 1. info 조합 구한 뒤 query에서 검색
# 통과
'''
정확성  테스트
테스트 1 〉	통과 (0.25ms, 10.4MB)
테스트 2 〉	통과 (0.24ms, 10.4MB)
테스트 3 〉	통과 (0.29ms, 10.4MB)
테스트 4 〉	통과 (1.44ms, 10.5MB)
테스트 5 〉	통과 (3.77ms, 10.5MB)
테스트 6 〉	통과 (3.70ms, 10.5MB)
테스트 7 〉	통과 (3.06ms, 10.8MB)
테스트 8 〉	통과 (31.02ms, 11.5MB)
테스트 9 〉	통과 (34.14ms, 11.6MB)
테스트 10 〉	통과 (32.90ms, 11.8MB)
테스트 11 〉	통과 (1.97ms, 10.6MB)
테스트 12 〉	통과 (3.77ms, 10.6MB)
테스트 13 〉	통과 (3.00ms, 10.7MB)
테스트 14 〉	통과 (16.94ms, 11MB)
테스트 15 〉	통과 (15.73ms, 11MB)
테스트 16 〉	통과 (1.93ms, 10.5MB)
테스트 17 〉	통과 (3.70ms, 10.6MB)
테스트 18 〉	통과 (15.70ms, 10.9MB)
효율성  테스트
테스트 1 〉	통과 (519.70ms, 42.8MB)
테스트 2 〉	통과 (533.00ms, 42.7MB)
테스트 3 〉	통과 (511.10ms, 42.5MB)
테스트 4 〉	통과 (513.81ms, 42.6MB)
'''
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    info_dict = {}
    for i in info:
        candidate = i.split()
        spec, score = candidate[:-1], int(candidate[-1])
        for n in range(5):
            for comb in combinations(spec, n):
                k = ''.join(comb)
                if k not in info_dict:
                    info_dict[k] = [score]
                else:
                    info_dict[k].append(score)        
    
    for v in info_dict.values():
        v.sort()
    
    for q in query:
        q = [elem for elem in q.split() if elem not in ['and', '-']]
        q_spec, q_score = ''.join(q[:-1]), int(q[-1])
        if q_spec in info_dict:
            score_list = info_dict[q_spec]
            idx = bisect_left(score_list, q_score)
            answer.append(len(score_list) - idx)
        else:
            answer.append(0)

    return answer

# 시간 초과


# 2. info_dict, score_list로 재구성한 뒤, 각 query 검색
# 시간 초과
'''
정확성  테스트
테스트 1 〉	통과 (0.09ms, 10.5MB)
테스트 2 〉	통과 (0.14ms, 10.5MB)
테스트 3 〉	통과 (0.36ms, 10.5MB)
테스트 4 〉	통과 (4.42ms, 10.6MB)
테스트 5 〉	통과 (14.96ms, 10.6MB)
테스트 6 〉	통과 (30.30ms, 10.6MB)
테스트 7 〉	통과 (16.02ms, 10.7MB)
테스트 8 〉	통과 (52.36ms, 14.1MB)
테스트 9 〉	통과 (48.62ms, 14.3MB)
테스트 10 〉	통과 (53.42ms, 13.6MB)
테스트 11 〉	통과 (9.61ms, 10.6MB)
테스트 12 〉	통과 (22.82ms, 10.7MB)
테스트 13 〉	통과 (10.50ms, 10.8MB)
테스트 14 〉	통과 (51.35ms, 12.1MB)
테스트 15 〉	통과 (46.02ms, 12.1MB)
테스트 16 〉	통과 (10.36ms, 10.7MB)
테스트 17 〉	통과 (21.97ms, 10.7MB)
테스트 18 〉	통과 (44.87ms, 12MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
'''

def solution(info, query):
    answer = []
    
    info_dict = {
        'cpp': set(),
        'java': set(),
        'python': set(),
        'backend': set(),
        'frontend': set(),
        'junior': set(),
        'senior': set(),
        'chicken': set(),
        'pizza': set(),
        '-': set()
    }
    score_dict = {}
    
    # info, score 해쉬 테이블 생성: O(n^2)
    for i, v in enumerate(info):
        info_dict['-'].add(i)
        for elem in v.split():
            if elem.isdigit():
                score_dict[i] = int(elem)
            else:
                info_dict[elem].add(i)    

    
    for q in query:
        v = q.replace('and ', '').split()
        (language, job, career, food), score = v[:-1], int(v[-1])
        candidates = info_dict[language] & \
                     info_dict[job] & \
                     info_dict[career] & \
                     info_dict[food] & \
                     {k for k, v in score_dict.items() if v >= score}
        answer.append(len(candidates))
        
    return answer