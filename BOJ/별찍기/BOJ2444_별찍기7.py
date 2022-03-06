N = int(input())

for n in range(1, 2*N):
    if n <= N:
        print(('*'*(2*n-1)).center(2*N-1).rstrip())
    else:
        print(('*'*(2*(2*N-n)-1)).center(2*N-1).rstrip())
