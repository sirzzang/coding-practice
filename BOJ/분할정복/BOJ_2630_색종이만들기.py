# n = int(input())
# squares = [''.join(input().split()) for _ in range(n)]
# print(squares)

# 하나로 이루어져 있는지 체크

def solution(squares_arr):
    squares = ''.join(squares_arr)
    if squares == len(squares)*squares[0]:
        print('탈출', squares[0])
        return

    sub_squares = []
    for row in range(2):
        part = squares_arr[row*(n//2):(row+1)*(n//2)]
        for col in range(2):
            sub_squares.append([p[col*(n//2):(col+1)*(n//2)] for p in part])

    for i in range(4):
        print(sub_squares[i])


# 4개로 나누기
if __name__ == '__main__':
    n = int(input())
    squares = ['11000011', '11000011', '00001100', '00001100', '10001111', '01001111', '00111111', '00111111']
    solution(squares)
