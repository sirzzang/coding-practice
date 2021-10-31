from collections import deque 

def solution(n, k):
    people = deque([i+1 for i in range(n)])

    i = 1
    answer = []
    while people:
        last = people.popleft()
        if i % k:
            people.append(last)
        else:
            answer.append(str(last))
        i += 1

    return answer

n, k = map(int, input().split())
print('<', end='')
answer = solution(n, k)
print(', '.join(answer), end='')
print('>', end='')
