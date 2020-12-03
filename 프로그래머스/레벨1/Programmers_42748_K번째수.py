def solution(array, commands):
    answer = []
    for command in commands:
        if command[0] == command[1]:
            answer.append(array[command[0]-1])
        else:
            start, end = command[0]-1, command[1]
            temp = array[start:end]
            temp.sort()
            answer.append(temp[command[-1]-1])            
    return answer