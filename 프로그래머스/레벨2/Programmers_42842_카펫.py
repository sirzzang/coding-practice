'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.10ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.2MB)
테스트 7 〉	통과 (0.08ms, 10.3MB)
테스트 8 〉	통과 (0.10ms, 10.3MB)
테스트 9 〉	통과 (0.09ms, 10.3MB)
테스트 10 〉	통과 (0.12ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
'''
def solution(brown, yellow):
    total = brown + yellow
    for height in range(3, int(total**(1/2))+1):
        if total % height == 0:
            width = total // height
            if (height-2) * (width-2) == yellow:
                return [width, height]