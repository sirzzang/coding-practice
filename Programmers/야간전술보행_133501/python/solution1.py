def solution(distance, scope, times):
    answer = distance
    
    for (s, t) in zip(scope, times):
        
        # 1초에는 모든 경비병이 근무함
        if s[0] == 1:
            return 1
        
        s.sort()
        (start, end), (work, rest) = s, t
        q = start // (work + rest)
        rest_start = (work + rest) * q + work + 1 # 휴식 전환 시간
        rest_end = (work + rest) * (q + 1) # 휴식 종료 시간
        
        # 경비병 감시 시작 구간에 근무 상태라면 지나갈 수 없음
        if start < rest_start:
            answer = min(answer, start)
            continue
        
        # 경비병 감시 종료 구간이 근무 상태라면 지나갈 수 없음
        if end > rest_end:
            answer = min(answer, rest_end + 1)
            
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	실패 (1.15ms, 10.3MB)
테스트 3 〉	통과 (0.77ms, 10.2MB)
테스트 4 〉	통과 (0.89ms, 10.4MB)
테스트 5 〉	통과 (0.38ms, 10.4MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.68ms, 10.2MB)
테스트 8 〉	통과 (1.22ms, 10.3MB)
테스트 9 〉	통과 (1.15ms, 10.2MB)
테스트 10 〉	실패 (0.09ms, 10MB)
테스트 11 〉	통과 (1.46ms, 10.3MB)
테스트 12 〉	통과 (0.36ms, 10.2MB)
테스트 13 〉	통과 (1.09ms, 10.3MB)
테스트 14 〉	실패 (1.09ms, 10.5MB)
'''