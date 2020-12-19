answer = [0, 0]

def solution(squares_arr):
    squares = ''.join(squares_arr)
    if squares == len(squares)*squares[0]:
        answer[int(squares[0])] += 1
        return

    half = len(squares_arr) // 2
    sub_squares = []
    for row in range(2):
        partition = squares_arr[row*half : (row+1)*half] # row로 partition
        for col in range(2):
            sub_squares.append([p[col*half : (col+1)*half] for p in partition])

    for i in range(4):
        solution(sub_squares[i])

if __name__ == '__main__':
    n = int(input())
    squares = ['11000011', '11000011', '00001100', '00001100', '10001111', '01001111', '00111111', '00111111']
    # squares = [''.join(input().split()) for _ in range(n)]
    solution(squares)
    print(answer[0])
    print(answer[1])