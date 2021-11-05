from itertools import permutations
from typing import List

'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.5MB)
테스트 2 〉	통과 (0.04ms, 10.5MB)
테스트 3 〉	통과 (0.09ms, 10.5MB)
테스트 4 〉	통과 (0.09ms, 10.4MB)
테스트 5 〉	통과 (0.09ms, 10.4MB)
테스트 6 〉	통과 (0.09ms, 10.5MB)
테스트 7 〉	통과 (0.10ms, 10.6MB)
테스트 8 〉	통과 (0.12ms, 10.5MB)
테스트 9 〉	통과 (0.12ms, 10.5MB)
테스트 10 〉	통과 (0.12ms, 10.5MB)
테스트 11 〉	통과 (0.12ms, 10.5MB)
테스트 12 〉	통과 (0.15ms, 10.5MB)
테스트 13 〉	통과 (0.14ms, 10.5MB)
테스트 14 〉	통과 (0.16ms, 10.5MB)
테스트 15 〉	통과 (0.17ms, 10.5MB)
테스트 16 〉	통과 (0.06ms, 10.5MB)
테스트 17 〉	통과 (0.06ms, 10.5MB)
테스트 18 〉	통과 (0.04ms, 10.5MB)
테스트 19 〉	통과 (0.04ms, 10.6MB)
테스트 20 〉	통과 (0.04ms, 10.5MB)
테스트 21 〉	통과 (0.07ms, 10.5MB)
테스트 22 〉	통과 (0.06ms, 10.5MB)
테스트 23 〉	통과 (0.03ms, 10.5MB)
테스트 24 〉	통과 (0.18ms, 10.6MB)
테스트 25 〉	통과 (0.17ms, 10.5MB)
테스트 26 〉	통과 (0.04ms, 10.5MB)
테스트 27 〉	통과 (0.17ms, 10.5MB)
테스트 28 〉	통과 (0.09ms, 10.5MB)
테스트 29 〉	통과 (0.08ms, 10.5MB)
테스트 30 〉	통과 (0.09ms, 10.5MB)
'''

def string_to_infix(expression: str) -> List[str]:
    infix = []
    digit = ''
    for char in expression:
        if char.isdigit():
            digit += char
        else:
            infix.append(digit)
            digit = ''
            infix.append(char)
    if digit:
        infix.append(digit)
    return infix

def infix_to_postfix(infix_arr: List[str], operand_rank: dict) -> List[str]:
    stack = []
    postfix = []
    for elem in infix_arr:
        if elem.isdigit():
            postfix.append(elem)
        else:
            while stack and operand_rank[elem] <= operand_rank[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(elem)
    while stack:
        postfix.append(stack.pop())
    return postfix

def calculate_postfix(postfix_arr: List[str]):
    stack = []
    for elem in postfix_arr:
        if elem.isdigit():
            stack.append(int(elem))
        else:
            b = stack.pop()
            a = stack.pop()
            if elem == '+':
                stack.append(a+b)
            elif elem == '-':
                stack.append(a-b)
            elif elem == '*':
                stack.append(a*b)
            else:
                stack.append(a/b)
    return stack[-1]

def solution(expression):
    answer = 0

    # 주어진 문자열을 중위표기 식의 각 연산자와 피연산자로 구성된 리스트로 변환
    infix = string_to_infix(expression)

    # 연산자 우선순위 경우의 수 도출
    operands = set(char for char in expression if not char.isdigit())
    ranks = permutations(operands, len(operands))

    # 연산자 우선순위에 따른 후위표기 연산식 계산
    for rank in ranks:
        priority = {v: i for i, v in enumerate(rank)}
        postfix = infix_to_postfix(infix, priority)
        result = calculate_postfix(postfix)
        if abs(result) > answer:
            answer = abs(result)
    
    return answer

# 다른 풀이
# - 연산자 우선순위에 따라 괄호 치고: split하는 단계, 문자열 포맷팅으로 괄호 치는 단계 주의
# - eval 함수를 통해 string 바로 계산값 구함
'''
정확성  테스트
테스트 1 〉	통과 (0.10ms, 10.2MB)
테스트 2 〉	통과 (0.10ms, 10.2MB)
테스트 3 〉	통과 (0.13ms, 10.3MB)
테스트 4 〉	통과 (0.16ms, 10.3MB)
테스트 5 〉	통과 (0.17ms, 10.2MB)
테스트 6 〉	통과 (0.16ms, 10.3MB)
테스트 7 〉	통과 (0.17ms, 10.3MB)
테스트 8 〉	통과 (0.24ms, 10.3MB)
테스트 9 〉	통과 (0.22ms, 10.3MB)
테스트 10 〉	통과 (0.31ms, 10.4MB)
테스트 11 〉	통과 (0.20ms, 10.2MB)
테스트 12 〉	통과 (0.42ms, 10.3MB)
테스트 13 〉	통과 (0.26ms, 10.3MB)
테스트 14 〉	통과 (0.45ms, 10.2MB)
테스트 15 〉	통과 (0.30ms, 10.3MB)
테스트 16 〉	통과 (0.16ms, 10.2MB)
테스트 17 〉	통과 (0.11ms, 10.3MB)
테스트 18 〉	통과 (0.17ms, 10.3MB)
테스트 19 〉	통과 (0.11ms, 10.3MB)
테스트 20 〉	통과 (0.18ms, 10.4MB)
테스트 21 〉	통과 (0.29ms, 10.3MB)
테스트 22 〉	통과 (0.29ms, 10.2MB)
테스트 23 〉	통과 (0.09ms, 10.2MB)
테스트 24 〉	통과 (0.32ms, 10.2MB)
테스트 25 〉	통과 (0.48ms, 10.3MB)
테스트 26 〉	통과 (0.09ms, 10.2MB)
테스트 27 〉	통과 (0.31ms, 10.4MB)
테스트 28 〉	통과 (0.52ms, 10.3MB)
테스트 29 〉	통과 (0.29ms, 10.3MB)
테스트 30 〉	통과 (0.29ms, 10.4MB)
'''
def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0] # 가장 우선순위가 낮은 연산자
        b = op[1] # 그 다음으로 우선순위가 낮은 연산자
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)] # 
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)


if __name__ == '__main__':
    solution("100-200*300-500+20")
    solution("50*6-3*2")


