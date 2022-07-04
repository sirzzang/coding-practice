def solution(id_list, report, k):
    answer = []
    report_count = {user_id : 0 for user_id in id_list}
    report_table = {user_id : [] for user_id in id_list}
    
    # 중복 제거
    report_list = list(set(report))
    
    for r in report_list:
        reporter, reportee = r.split()
        report_count[reportee] += 1 # 피신고 횟수
        report_table[reporter].append(reportee) # 신고자별 신고 명단
    
    # 신고 처리횟수 집계
    for user_id in id_list:
        if not report_table[user_id]:
            answer.append(0)
        else:        
            cnt = 0
            for reportee_id in report_table[user_id]:
                if report_count[reportee_id] >= k:
                    cnt += 1
            answer.append(cnt)        
    
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (133.26ms, 39.6MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.04ms, 10.2MB)
테스트 6 〉	통과 (0.91ms, 10.4MB)
테스트 7 〉	통과 (1.40ms, 10.7MB)
테스트 8 〉	통과 (1.82ms, 11MB)
테스트 9 〉	통과 (66.38ms, 24.1MB)
테스트 10 〉	통과 (56.40ms, 24.1MB)
테스트 11 〉	통과 (172.10ms, 39.5MB)
테스트 12 〉	통과 (0.23ms, 10.3MB)
테스트 13 〉	통과 (0.23ms, 10.3MB)
테스트 14 〉	통과 (44.70ms, 22.5MB)
테스트 15 〉	통과 (75.45ms, 32.8MB)
테스트 16 〉	통과 (0.13ms, 10.2MB)
테스트 17 〉	통과 (0.36ms, 10.3MB)
테스트 18 〉	통과 (0.36ms, 10.2MB)
테스트 19 〉	통과 (0.97ms, 10.5MB)
테스트 20 〉	통과 (51.11ms, 22.5MB)
테스트 21 〉	통과 (70.49ms, 32.8MB)
테스트 22 〉	통과 (0.01ms, 10.2MB)
테스트 23 〉	통과 (0.01ms, 10.2MB)
테스트 24 〉	통과 (0.01ms, 10.1MB)
'''