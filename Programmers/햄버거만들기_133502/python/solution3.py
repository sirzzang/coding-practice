def solution(ingredient):
    answer = 0
    
    stack = []
    burger = [1, 2, 3, 1]
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == burger:
            answer += 1
            stack = stack[:-4]
        # print(f"ingredient: {d}, stack: {stack}, answer: {answer}")    
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10.3MB)
테스트 3 〉	통과 (1909.29ms, 18.7MB)
테스트 4 〉	통과 (8813.12ms, 29.1MB)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	통과 (4318.97ms, 23.4MB)
테스트 7 〉	통과 (7207.24ms, 27.4MB)
테스트 8 〉	통과 (4493.54ms, 24.2MB)
테스트 9 〉	통과 (2511.00ms, 20.7MB)
테스트 10 〉	통과 (1.90ms, 10.3MB)
테스트 11 〉	통과 (1227.55ms, 17.7MB)
테스트 12 〉	실패 (시간 초과)
테스트 13 〉	통과 (0.00ms, 10.2MB)
테스트 14 〉	통과 (0.00ms, 10.2MB)
테스트 15 〉	통과 (0.00ms, 10.2MB)
테스트 16 〉	통과 (0.00ms, 10.3MB)
테스트 17 〉	통과 (0.00ms, 10.2MB)
'''