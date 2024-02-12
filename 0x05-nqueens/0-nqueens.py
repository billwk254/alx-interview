#!/usr/bin/python3
"""N Queens problem."""
import sys


def is_safe(board, row, col, N):
    """Check if it is safe to place a queen at board[row][col]."""
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N):
    """Solve N Queens problem using backtracking."""
    # If all queens are placed then return True
    if col >= N:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1

            # recur to place rest of the queens
            if solve_nqueens_util(board, col + 1, N):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution
            # then remove queen from board[i][col]
            board[i][col] = 0

    # if queen can not be place in any row in this column col then return False
    return False


def solve_nqueens(N):
    """Solve N Queens problem."""
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board
    board = [[0] * N for _ in range(N)]

    if not solve_nqueens_util(board, 0, N):
        print("No solution exists")
        return

    # Print the solution
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("[{}, {}]".format(i, j), end=" ")
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)