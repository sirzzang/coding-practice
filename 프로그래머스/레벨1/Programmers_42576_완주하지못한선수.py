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