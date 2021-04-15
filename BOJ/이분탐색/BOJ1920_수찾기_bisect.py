import sys
import bisect

n = int(sys.stdin.readline().strip('\n'))
my_list = list(map(int, sys.stdin.readline().strip('\n').split()))
my_list.sort()
m = int(sys.stdin.readline().strip('\n'))
nums = list(map(int, sys.stdin.readline().strip('\n').split()))

for num in nums:
    idx = bisect.bisect_left(my_list, num)
    if idx >= n:
        print(0)
    else:
        if num == my_list[idx]:
            print(1)
        else:
            print(0)
