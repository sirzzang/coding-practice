# 개미수열
'''재귀로 어떻게 string을 더해 가는가'''


def countAndSay(n: int) -> str:
    if n == 1:
        return "1"

    i = 1
    temp = ''
    while i <= n:
        print(i, temp)
        temp += str(i)
        i += 1
        countAndSay(i)


countAndSay(4)
