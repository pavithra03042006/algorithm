def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "_" for cell in row))
    print()

def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j]:
            return False

    return True

def solve_n_queens(board, row):
    if row == len(board):
        print_board(board)
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_n_queens(board, row + 1):
                return True
            board[row][col] = 0  

    return False

n = int(input("Enter the size of the board: "))
board = [[0] * n for _ in range(n)]

if not solve_n_queens(board, 0):
    print("No solution exists.")
