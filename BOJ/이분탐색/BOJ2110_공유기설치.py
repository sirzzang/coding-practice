houses = [1, 3, 7, 11, 17, 21, 35, 64, 70, 85]
# houses.sort()
c = 8

left = 0
right = len(houses)-1
cnt = 0

while left <= right:
    mid = (left + right)//2
    print("공유기 설치 위치:", houses[mid])

    if houses[mid] <= (houses[left] + houses[right])/2:
        right = mid - 1
    else:
        left = mid + 1

    cnt += 1
    if cnt == c-2:
        break
