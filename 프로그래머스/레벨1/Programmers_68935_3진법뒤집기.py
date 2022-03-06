# 3진법 거꾸로
def num_to_reverse_ternary(n):
    ternary = ''
    while n:
        ternary += str(n%3)
        n //= 3
    return ternary

# 10진법으로
def solution(n):
    answer = 0
    ternary = num_to_reverse_ternary(n)
    temp = len(ternary)-1
    for num in ternary:
        if num == '0':
            temp -= 1
            continue
        else:
            answer += int(num) * (3**temp)
            temp -= 1        
    return answer