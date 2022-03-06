'''
정확성  테스트
테스트 1 〉	통과 (0.40ms, 10.2MB)
테스트 2 〉	통과 (0.52ms, 10.4MB)
테스트 3 〉	통과 (0.46ms, 10.4MB)
테스트 4 〉	통과 (0.44ms, 10.3MB)
테스트 5 〉	통과 (0.48ms, 10.3MB)
테스트 6 〉	통과 (0.42ms, 10.4MB)
테스트 7 〉	통과 (0.42ms, 10.3MB)
테스트 8 〉	통과 (0.53ms, 10.4MB)
테스트 9 〉	통과 (0.45ms, 10.4MB)
'''


def solution(absolutes, signs):
    answer = 0
    for sign, num in zip(signs, absolutes):
        if sign:
            answer += int(f'+{num}')
        else:
            answer += int(f'-{num}')
    return answer
