# 시간초과
'''
def solution(string, flag):
    while flag in string:
        string = string.replace(flag, '')

    if not string:
        return 'FRULA'
    return string
'''
'''
import re
def solution(string, flag):
    s = string
    while flag in s:
        s = re.sub(flag, '', s)

    if not s:
        return 'FRULA'
    return s
'''




import sys
def solution(string, flag):
    stack = []

    while string:
        stack.append(string.pop())
        if len(stack) >= len(flag) and ''.join(stack[-len(flag):]) == flag[::-1]:
            for _ in range(len(flag)):
                stack.pop()

    if not stack:
        return 'FRULA'
    return ''.join(stack[::-1])


if __name__ == '__main__':
    # print(solution(input(), input()))
    print(solution(list(sys.stdin.readline().strip('\n')),
                   sys.stdin.readline().strip('\n')))
