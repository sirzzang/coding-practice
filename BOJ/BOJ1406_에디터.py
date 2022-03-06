# PyPy3로도 시간 초과
edit = input()
m = int(input())
cursor = len(edit) # 초기 커서 위치
for _ in range(m):
    command = input()
    if command[0] == 'P':
        char = command.split()[-1]
        edit = edit[:cursor] + char + edit[cursor:]
        cursor += 1   
    elif command[0] == 'L':
        if not cursor:
            continue
        cursor -= 1
    elif command[0] == 'D':
        if cursor == len(edit):
            continue
        cursor += 1
    else:
        if not cursor: # 커서 맨 앞일 때 무시
            continue
        edit = edit[:cursor-1] + edit[cursor:]
        cursor -= 1
print(edit)