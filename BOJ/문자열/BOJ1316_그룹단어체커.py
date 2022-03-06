def group_checker(text):
    for char in set(text):
        start, end = text.index(char), len(text)-text[::-1].index(char)-1
        check = text[start:end+1]
        if len(set(check)) > 1:
            return False
    return True

n = int(input())
answer = 0
for _ in range(n):
    answer += group_checker(input())
print(answer)
