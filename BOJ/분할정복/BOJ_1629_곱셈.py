answer = 1

def solution(a, b, c):
    global answer

    if b == 1:
        return

    # print(answer*a, b, c)
    answer = (answer*a)%12
    solution(a, b-1, c)

a, b, c = map(int, input().split())
solution(a, b, c)
print(answer)