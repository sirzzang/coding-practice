def solution(k, ranges):
    answer = []
    
    # 우박 수열에 대한 정적분 값
    integral = []
    while k != 1:
        prev = k
        if k % 2:
            k = k * 3 + 1
        else:
            k //= 2
        integral.append((prev + k) / 2)

    # 정적분 결과 목록 구하기
    for r in ranges:
        start, end = r[0], len(integral) + r[1]
        if start == end:
            answer.append(0)
        elif start > end:
            answer.append(-1)
        else:
            answer.append(sum(integral[i] for i in range(start, end)))

    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.68ms, 10.2MB)
테스트 3 〉	통과 (19.31ms, 12.2MB)
테스트 4 〉	통과 (1.57ms, 10.6MB)
테스트 5 〉	통과 (0.66ms, 10.2MB)
테스트 6 〉	통과 (4.18ms, 10.7MB)
테스트 7 〉	통과 (30.33ms, 12MB)
테스트 8 〉	통과 (48.35ms, 12.4MB)
테스트 9 〉	통과 (0.21ms, 10.2MB)
테스트 10 〉	통과 (5.58ms, 10.8MB)
'''