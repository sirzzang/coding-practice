N = int(input())

for n in range(1, 2*N, 2):
    print(('*'*n).center(2*N-1).rstrip())
