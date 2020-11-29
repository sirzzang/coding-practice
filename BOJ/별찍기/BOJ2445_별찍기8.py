N = int(input())

for n in range(1, 2*N):
    if n <= N:
        print(('*'*n + ' '*(2*(N-n)) + '*'*n).strip())
    else:
        print(('*'*(2*N-n) + ' '*2*(n-N) + '*'*(2*N-n)).strip())
