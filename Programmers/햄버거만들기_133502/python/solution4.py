def solution(ingredient):
    answer = 0
    
    stack = []
    burger = [1, 2, 3, 1]
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == burger:
            answer += 1
            for i in range(4):
                stack.pop()
            # stack = stack[:-4]
        # print(f"ingredient: {d}, stack: {stack}, answer: {answer}")    
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (43.00ms, 14.8MB)
테스트 4 〉	통과 (92.10ms, 20.4MB)
테스트 5 〉	통과 (111.88ms, 23.1MB)
테스트 6 〉	통과 (64.48ms, 17.5MB)
테스트 7 〉	통과 (82.14ms, 19.4MB)
테스트 8 〉	통과 (65.92ms, 17.8MB)
테스트 9 〉	통과 (48.69ms, 15.6MB)
테스트 10 〉	통과 (1.20ms, 10.5MB)
테스트 11 〉	통과 (37.20ms, 14.3MB)
테스트 12 〉	통과 (134.37ms, 26.7MB)
'''