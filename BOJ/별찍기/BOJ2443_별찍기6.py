N = int(input())

for n in range(2*N-1, 0, -2):
    print(('*'*n).center(2*N-1).rstrip())
