'''
있는지 없는지 찾기만 하면 되는 게 아니라,
있으면 몇 개가 있는지 찾아야 하는 문제
'''

# 정렬 방향만 반대로 하면 안 되나? -> 정렬 두 번 해서 저장해 놔야 하고, 내림차순 정렬했을 때 인덱스 순이 안 맞음


def binary_search_upper_bound(arr, target):
    left = 0
    right = len(arr) - 1

    # print(f'finding {target} upper bound')
    while left < right:
        # print(f'left: {left}, right: {right}')
        mid = (left + right)//2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left


def binary_search_lower_bound(arr, target):
    left = 0
    right = len(arr) - 1

    # print(f'finding {target} lower bound')
    while left < right:
        # print(f'left: {left}, right: {right}')
        mid = (left + right)//2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


n = input()
cards = list(map(int, input().split()))
m = input()
nums = list(map(int, input().split()))

cards.sort()

print(cards)

for num in nums:
    print(num, binary_search_lower_bound(cards, num),
          binary_search_upper_bound(cards, num))
