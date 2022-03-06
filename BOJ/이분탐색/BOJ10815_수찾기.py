def binary_search(arr, target):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return 0


n = input()
cards = list(map(int, input().split()))
m = input()
numbers = list(map(int, input().split()))

cards.sort()
for number in numbers:
    print(binary_search(cards, number), end=' ')
