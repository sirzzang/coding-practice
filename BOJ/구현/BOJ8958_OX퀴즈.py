'''
메모리 29076KB
시간	72ms
'''


def solution(answer_str):
    score = 0
    cur = 0
    for i in range(len(answer_str)):
        if answer_str[i] == "O":
            cur += 1
            score += cur
        else:
            cur = 0
    return score


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        print(solution(input()))
