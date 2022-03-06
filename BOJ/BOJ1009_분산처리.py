units = {2: [2, 4, 8, 6], 3: [3, 9, 7, 1], 4: [4, 6],
         7: [7, 9, 3, 1], 8: [8, 4, 2, 6], 9: [9, 1]}
t = int(input())


for _ in range(t):
    a, b = map(int, input().split())
    a = int(str(a)[-1])
    if a == 1:
        print(1)
    elif a == 5:
        print(5)
    elif a == 6:
        print(6)
    elif a % 10 == 0:
        print(10)
    else:
        idx = b % len(units[a])
        print(units[a][idx-1])
