'''
min 거리만 최대가 되게 하면 되니까 반씩 줄여 가며 더 먼 쪽은 그냥 버리는 방식을 썼는데,
- 일단 공유기 설치 대수가 안 맞을 수도 있고, (지금의 경우 17, 3, 1만 설치하고 끝나 버림)
- 처음에 중간으로 갈 때 17에 놔야 하는지 21에 놔야 하는지 결정할 로직도 필요
'''

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
