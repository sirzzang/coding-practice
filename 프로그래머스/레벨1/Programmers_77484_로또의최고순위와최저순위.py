'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.00ms, 10.2MB)
테스트 11 〉	통과 (0.00ms, 10.2MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.00ms, 10.3MB)
테스트 14 〉	통과 (0.00ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.1MB)
'''


def solution(lottos, win_nums):
    answer = []

    cnt = 0  # 맞춘 개수
    for num in win_nums:
        if num in lottos:
            cnt += 1

    unknown = lottos.count(0)  # 모르는 번호 개수

    # 전부 다 맞춘 경우
    if cnt == 6:
        return [1, 1]

    # 전부 다 모르는 경우
    elif unknown == 6:
        return [1, 6]

    # 전부 다 틀린 경우
    elif cnt == 0 and unknown == 0:
        return [6, 6]

    return [7-cnt-unknown, 7-cnt]
