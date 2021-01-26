'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.04ms, 10.2MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.05ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (1.19ms, 10.6MB)
테스트 2 〉	통과 (0.85ms, 10.4MB)
테스트 3 〉	통과 (2.15ms, 10.6MB)
테스트 4 〉	통과 (0.09ms, 10.2MB)
테스트 5 〉	통과 (2.55ms, 10.8MB)
'''


def solution(routes):
    answer = 0
    # 진입 빠른 순(동 순위 시 진출 빠른 순)으로 정렬
    routes.sort(key=lambda x: (x[0], x[1]))

    loc = routes[0][1]
    for r in routes:
        # 직전 진입 차가 현재 진입보다 빠르게 빠져 나간 경우
        if loc < r[0]:
            answer += 1
            loc = r[1]
        # 현재 진출보다 직전 진입 차의 진출이 더 늦는 경우
        if loc >= r[1]:
            loc = r[1]

    return answer + 1  # 1대는 무조건 설치
