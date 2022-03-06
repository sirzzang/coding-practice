from typing import List

def infix_to_postfix(arr: List[str]) -> List[str]:
    stack = []
    postfix = []
    ranks = {'(': 0, '+': 1, '-': 1, '*': 2, '/':2}
    for elem in arr:
        if elem.isdigit():
            postfix.append(elem)
        elif elem == '(':
            stack.append(elem)
        elif elem == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and ranks[elem] <= ranks[stack[-1]]:
                postfix.append(stack.pop())
                stack.append(elem)
            stack.append(elem)
    while stack:
        postfix.append(stack.pop())
    return postfix

def calculate_postfix(postfix_arr: List[str]) -> int:
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


calculate_postfix(infix_to_postfix(['(', '(', '(', '100', '-', '(', '200', '*', '300', ')', ')', '-', '500', ')', '+', '(', '20', '/', '2', ')', ')']))
calculate_postfix(infix_to_postfix(['(', '3', '+', '(', '(', '5', '*', '2', ')', '/', '(', '7', '-', '2', ')', ')', ')']))