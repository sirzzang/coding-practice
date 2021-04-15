import sys


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


n = int(sys.stdin.readline().strip('\n'))
my_list = list(map(int, sys.stdin.readline().strip('\n').split()))
my_list.sort()
m = int(sys.stdin.readline().strip('\n'))
nums = list(map(int, sys.stdin.readline().strip('\n').split()))

for n in nums:
    print(binary_search(my_list, n))
