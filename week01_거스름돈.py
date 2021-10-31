def solution(n):
    # 거슬러 줄 수 없는 경우
    if n == 1 or n == 3:
        return -1
    
    q, r = divmod(n, 5)
    if r == 0:
        return q
    elif r == 1 or r == 3:
        return q-1+(r+5)//2
    else:
        return q + r//2

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(13))
print(solution(14))
print(solution(15))

amount = int(input())
print(solution(amount))