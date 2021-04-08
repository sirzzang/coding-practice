def cycle(n):
    given = n  # string

    if int(n) < 10:
        n = '0' + str(n)  # string
    n = str(sum([int(char) for char in list(n)]))  # string

    return given[-1] + n[-1]


num = input()
temp = cycle(num)
cnt = 1
while int(temp) != int(num):
    temp = cycle(temp)
    cnt += 1
    print(temp)
print('최종', cnt)
