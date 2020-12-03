def solution(strings, n):
    answer = sorted(strings, key=lambda x:(x[n], x)) # 두 번째 기준: 사전 순으로 앞선 문자열
    return answer