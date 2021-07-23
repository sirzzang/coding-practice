from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    # for row in range(9):
    #     repeat_checker = ''
    #     for i in range(9):
    #         print(f'{row}행', i, board[row][i])
    #         if board[row][i].isdigit():
    #             if board[row][i] in repeat_checker:
    #                 return False
    #             repeat_checker += board[row][i]

    # for col in range(9):
    #     repeat_checker = ''
    #     for i in range(9):
    #         print(f'{col}열', i, board[i][col])
    #         if board[i][col].isdigit():
    #             if board[i][col] in repeat_checker:
    #                 return False
    #             repeat_checker += board[i][col]

    for i in range(3):
        for j in range(3):
            print(board[j][i*3:(i+1)*3])


isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".",
                                                                                                                                                                                                            "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
