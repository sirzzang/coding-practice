k, n = map(int, input().split())
wires = [int(input()) for _ in range(k)]

left = 1  # left 0부터 시작하면 ZeroDivisionError: k=1, n=1, wires=[1]
right = max(wires)

while left <= right:
    mid = (left + right)//2

    cnt = sum(wire//mid for wire in wires)

    if cnt >= n:
        left = mid + 1
    else:
        right = mid - 1

print(right)
