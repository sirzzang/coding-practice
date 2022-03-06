import sys
from bisect import *


n = sys.stdin.readline()
cards = list(map(int, sys.stdin.readline().strip('\n').split()))
m = sys.stdin.readline()
nums = list(map(int, sys.stdin.readline().strip('\n').split()))
cards.sort()

for num in nums:
    print(bisect_right(cards, num) - bisect_left(cards, num), end=' ')
