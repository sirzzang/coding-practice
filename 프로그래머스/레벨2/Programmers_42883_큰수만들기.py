'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.4MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (0.13ms, 10.4MB)
테스트 4 〉	통과 (0.61ms, 10.3MB)
테스트 5 〉	통과 (1.02ms, 10.4MB)
테스트 6 〉	통과 (10.68ms, 10.4MB)
테스트 7 〉	통과 (28.55ms, 10.8MB)
테스트 8 〉	통과 (61.56ms, 11.2MB)
테스트 9 〉	통과 (137.18ms, 14.2MB)
테스트 10 〉	통과 (309.87ms, 14MB)
테스트 11 〉	통과 (0.03ms, 10.4MB)
테스트 12 〉	통과 (0.02ms, 10.3MB)
'''
def solution(number, k):
    stack = [number[0]] # 스택 초기값 : 첫 번째 수 선택한 것으로 간주.
    for n in number[1:]:
        while stack and int(n)>int(stack[-1]) and k>0: # pop 조건
            stack.pop()
            k -= 1
        stack.append(n) # pop하지 않으면 append.
        if len(stack) == len(number) - k: # 선택 과정 종료 조건
            break
    answer = ''.join(stack)
    return answer