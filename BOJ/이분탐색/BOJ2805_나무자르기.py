n, m = map(int, input().split())

trees = list(map(int, input().split()))
trees.sort()

left = 1
right = trees[-1]

while left <= right:
    mid = (left + right) // 2
    total = sum(tree-mid for tree in trees if tree >= mid)

    if total >= m: # 조건 충족 시 최댓값 찾기 위해 오른쪽 구간
        left = mid + 1
    else: # 조건 미충족 시 최댓값 찾기 위해 왼쪽 구간에 대해
        right = mid - 1 

print(left)