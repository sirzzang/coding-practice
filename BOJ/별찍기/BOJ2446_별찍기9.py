N = int(input())

for n in range(1, 2*N):
    if n <= N:
        print((' '*(n-1) + '*'*(2*(N-n)+1)).rstrip())
    else:
        print((' '*(2*N-n-1) + '*'*(2*(n-N+1)-1)).rstrip())
