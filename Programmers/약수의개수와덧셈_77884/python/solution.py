def solution(left, right):
    if left == right:
        return 0
    
    answer = 0
    for n in range(left, right + 1):
        if n**(1/2) == int(n**(1/2)):
            answer -= n
        else:
            answer += n
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.39ms, 10.2MB)
테스트 2 〉	통과 (0.13ms, 10.4MB)
테스트 3 〉	통과 (0.17ms, 10.4MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.31ms, 10.2MB)
테스트 6 〉	통과 (0.05ms, 10.3MB)
테스트 7 〉	통과 (0.04ms, 10.2MB)
'''