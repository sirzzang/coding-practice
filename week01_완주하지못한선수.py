# 정렬 후 completion 리스트에 없는 participant 요소 찾기
'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.27ms, 10.3MB)
테스트 4 〉	통과 (0.63ms, 10.3MB)
테스트 5 〉	통과 (0.54ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (36.35ms, 18MB)
테스트 2 〉	통과 (54.58ms, 22.1MB)
테스트 3 〉	통과 (76.41ms, 24.7MB)
테스트 4 〉	통과 (83.71ms, 26.3MB)
테스트 5 〉	통과 (76.73ms, 26.2MB)
'''
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]

# 참가자 명단과 완주자 명단
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.21ms, 10.1MB)
테스트 4 〉	통과 (0.44ms, 10.3MB)
테스트 5 〉	통과 (0.39ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (20.05ms, 21.8MB)
테스트 2 〉	통과 (28.44ms, 25.2MB)
테스트 3 〉	통과 (44.12ms, 27.7MB)
테스트 4 〉	통과 (50.98ms, 33.8MB)
테스트 5 〉	통과 (50.88ms, 34MB)
'''

def solution(participant, completion):
    participant_dict = {}
    
    # 참가자 명단
    for p in participant:
        if p not in participant_dict:
            participant_dict[p] = 1
        else:
            participant_dict[p] += 1
            
    # 완주자
    for c in completion:
        participant_dict[c] -= 1
        
    for k, v in participant_dict.items():
        if v:
            return k