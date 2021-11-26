'''
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.3MB)
테스트 2 〉	통과 (0.06ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (5.83ms, 10.5MB)
테스트 5 〉	통과 (50.78ms, 10.4MB)
테스트 6 〉	실패 (1.11ms, 10.3MB)
테스트 7 〉	통과 (1.74ms, 10.4MB)
테스트 8 〉	통과 (6.11ms, 10.5MB)
테스트 9 〉	통과 (0.04ms, 10.3MB)
테스트 10 〉	실패 (0.67ms, 10.3MB)
테스트 11 〉	실패 (6.19ms, 10.5MB)
'''

import pprint

# m, n, board = 6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
# m, n, board = 4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]
# m, n, board = 6, 5, ["CCZXZ", "CCZXZ", "XXZXZ", "AAZAA", "AAAAA", "ZAAXX"]
m, n, board = 8, 5, ["HGNHU", "CRSHV", "UKHVL", "MJHQB", "GSHOT", "MQMJJ", "AGJKK", "QULKK"]

board = [list(b) for b in board]
answer = 0
i = 1
while True:
    del_position = []
    pprint.pprint(board)
    for row in range(m-1):
        for col in range(n-1):
            if board[row][col] and len(set(board[row][col:col+2]+board[row+1][col:col+2])) == 1:
                del_position.extend([(row, col), (row, col+1), (row+1, col), (row+1, col+1)])
    if not del_position:
        break

    answer += len(set(del_position))
    del_position.sort(key=lambda x: (x[1], x[0]))

    for row, col in del_position:
        while row :
            if board[row-1][col]:
                board[row][col] = board[row-1][col]
                board[row-1][col] = None
            row -= 1

pprint.pprint(board)
print(answer)
