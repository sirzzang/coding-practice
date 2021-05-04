# 풀이 2
# - 괄호 검사 시 전부 분기처리 괜찮은가?
# - 회전도 O(N)인데?
# - 괄호 검사 시 solution에서 괄호 개수 맞는지 확인했더니 통과
'''
정확성  테스트
테스트 1 〉	통과 (7.14ms, 10.2MB)
테스트 2 〉	통과 (4.27ms, 10.2MB)
테스트 3 〉	통과 (6.13ms, 10.2MB)
테스트 4 〉	통과 (5.34ms, 10.2MB)
테스트 5 〉	통과 (18.71ms, 10.3MB)
테스트 6 〉	통과 (7.22ms, 10.2MB)
테스트 7 〉	통과 (10.67ms, 10.2MB)
테스트 8 〉	통과 (13.58ms, 10.2MB)
테스트 9 〉	통과 (26.75ms, 10.2MB)
테스트 10 〉	통과 (37.10ms, 10.2MB)
테스트 11 〉	통과 (57.03ms, 10.3MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.00ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
'''


def check_parentheses(brackets):
    stack = []
    for bracket in brackets:

        # 여는 괄호의 경우 stack에 추가
        if bracket in '({[':
            stack.append(bracket)
        else:
            # 닫는 괄호인데 여는 괄호가 없을 경우 틀린 괄호 문자열
            if not stack:
                return False
            # 올바른 짝일 경우에만 stack에서 pop
            elif bracket == ')':
                if stack[-1] != '(':
                    return False
                stack.pop()
            elif bracket == '}':
                if stack[-1] != '{':
                    return False
                stack.pop()
            else:
                if stack[-1] != '[':
                    return False
                stack.pop()
        # print(bracket, stack)

    return True


def solution(s):

    if s.count('(') + s.count('{') + s.count('[') !=\
            s.count(')')+s.count('}')+s.count(']'):
        return 0

    answer = 0
    s_len = len(s)

    # 회전하며 괄호 검사
    for i in range(s_len):
        rotate = s[i:s_len] + s[0:i]
        answer += check_parentheses(rotate)

    return answer
