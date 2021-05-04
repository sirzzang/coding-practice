# 풀이 1
# - 괄호 검사 시 전부 분기처리 괜찮은가?
# - 회전도 O(N)인데?
'''
정확성  테스트
테스트 1 〉	통과 (7.12ms, 10.2MB)
테스트 2 〉	통과 (3.97ms, 10.3MB)
테스트 3 〉	통과 (4.19ms, 10.2MB)
테스트 4 〉	통과 (5.09ms, 10.2MB)
테스트 5 〉	통과 (19.30ms, 10.2MB)
테스트 6 〉	통과 (7.98ms, 10.3MB)
테스트 7 〉	통과 (10.06ms, 10.2MB)
테스트 8 〉	통과 (14.12ms, 10.3MB)
테스트 9 〉	통과 (27.20ms, 10.2MB)
테스트 10 〉	통과 (38.84ms, 10.2MB)
테스트 11 〉	통과 (61.96ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	실패 (0.01ms, 10.2MB)
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

    answer = 0
    s_len = len(s)

    # 회전하며 괄호 검사
    for i in range(s_len):
        rotate = s[i:s_len] + s[0:i]
        answer += check_parentheses(rotate)
        # print(check_parentheses(rotate))

    return answer
