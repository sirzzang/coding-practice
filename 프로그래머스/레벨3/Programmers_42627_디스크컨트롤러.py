'''
정확성  테스트
테스트 1 〉	통과 (18.94ms, 10.2MB)
테스트 2 〉	통과 (15.07ms, 10.2MB)
테스트 3 〉	통과 (10.65ms, 10.3MB)
테스트 4 〉	통과 (10.67ms, 10.2MB)
테스트 5 〉	통과 (25.50ms, 10.3MB)
테스트 6 〉	통과 (0.07ms, 10.2MB)
테스트 7 〉	통과 (8.78ms, 10.3MB)
테스트 8 〉	통과 (5.84ms, 10.2MB)
테스트 9 〉	통과 (2.08ms, 10.2MB)
테스트 10 〉	통과 (21.22ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.03ms, 10.3MB)
테스트 14 〉	통과 (0.02ms, 10.3MB)
테스트 15 〉	통과 (0.02ms, 10.2MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.1MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
테스트 20 〉	통과 (0.00ms, 10.2MB)
'''
def solution(jobs):
    answer = 0
    prev = 0
    n_jobs = len(jobs)
    while jobs:
        temp = [job for job in jobs if job[0] <= prev]  # 필터링
        if temp:
            temp.sort(key=lambda x: x[1])
            cur = jobs.pop(jobs.index(temp[0]))  # 시간 효율성?
        else:
            jobs.sort(key=lambda x: (x[0], x[1]))  # 필터링된 애들 없는 경우: 이전에 작업 진행 중이지 않음
            cur = jobs.pop(0)
            prev = cur[0]

        prev += cur[1]
        answer += prev - cur[0]
        # print(f"현재 작업: {cur}, 종료: {prev}")
    return answer // n_jobs