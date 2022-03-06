'''24ms, 14.3MB'''

def isValid(s: str) -> bool:
    print()
    stack = []
    pairs = {")": '(', '}': '{', ']': '['}
    for bracket in s:
        print(bracket, stack)
        if bracket in pairs.values():
            stack.append(bracket)
        else:
            if not stack:
                return False
            if stack[-1] != pairs[bracket]:
                return False
            stack.pop() # 올바른 괄호인 경우
    
    # 개수가 맞지 않는 경우
    if stack:
        return False
    return True

assert isValid("()") == True
assert isValid("()[]{}") == True
assert isValid("(]") == False
assert isValid("([)]") == False
assert isValid("{[]}") == True

