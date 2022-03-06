def solution(s):
    answer = True
    s = s.lower() # 소문자로 바꾸기
    if s.count('p') != s.count('y'):
        return False
    return True