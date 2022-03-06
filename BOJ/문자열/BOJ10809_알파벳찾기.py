import sys

myStr = sys.stdin.readline()

alphabts = 'abcdefghijklmnopqrstuvwxyz'
for a in alphabts:
    print(myStr.find(a), end=' ')
