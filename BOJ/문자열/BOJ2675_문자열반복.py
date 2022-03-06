t = int(input())

for _ in range(t):
    user_input = input().split()
    r, string = int(user_input[0]), user_input[1]
    answer = ''
    for s in string:
        answer += s*r
    print(answer)
