import sys

user_input = list(map(lambda x: x.strip('\n'), sys.stdin.readlines()))
f_num, f_names = int(user_input[0]), user_input[1:]
f_len = len(f_names[0])

chars = {i: set() for i in range(f_len)}
for i in range(f_len):
    for j in range(f_num):
        chars[i].add(f_names[j][i])

answer = ''
for v in chars.values():
    if len(v) > 1:
        answer += '?'
    else:
        answer += list(v)[0]
print(answer)
