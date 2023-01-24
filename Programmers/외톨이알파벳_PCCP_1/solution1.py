def solution(input_string):
        
    char_dict = {}
    prev = ''
    for i, v in enumerate(input_string):
        
        # 뭉쳐서 등장한 경우는 체크하지 않음
        if v == prev:
            continue
            
        # 문자별 첫 등장 위치 기록
        if v not in char_dict:
            char_dict[v] = []
        char_dict[v].append(i)        
        prev = v

    answer = "".join(sorted([k for k in char_dict if len(char_dict[k]) >= 2]))
    
    return answer if answer else "N"

'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.1MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.23ms, 10.3MB)
테스트 5 〉	통과 (0.12ms, 10.2MB)
테스트 6 〉	통과 (0.12ms, 10.1MB)
테스트 7 〉	통과 (0.08ms, 10.1MB)
테스트 8 〉	통과 (0.13ms, 10.1MB)
테스트 9 〉	통과 (0.11ms, 10.2MB)
테스트 10 〉	통과 (0.10ms, 10MB)
'''