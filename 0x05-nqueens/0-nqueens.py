#!/usr/bin/python3
"""Defines the functions for solving the nqueens puzzle."""
import sys


def main():
    """Entry point function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    N = sys.argv[1]
    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    nqueens_puzzle(N)


def nqueens_puzzle(N):
    """
    The N-queens puzzle.
        The challenge of placing N non-attacking queens on an NxN chessboard.

    Usage :
        >>> ./0-nqueens.py N

    Args :
        N: The number of queens.

    Execptions :
        ValueError: N must be be a number | N must be an integer >= 4

    Attributes :
        board type(list): A list of lists representing the chessboard.
        results type(list): A list containing all possible solutions.

    Solutions are represented in this format [[r, c], [r, c], [r, c], [r, c]]
    where `r` and `c` represent the row and column, respectively, where a
    queen must be placed on the chessboard.
    """

    # Initialize the chess board & the output results list matrix
    results = []
    board = [-1] * N

    # solve_puzzle(board, 0, N, results)

    for solution in results:
        print(solution)


# def solve_puzzle(board, row, N, results):
#     """
#     Solves the N-Queens puzzle recursively.
#     Args:
#     - board (list): The current working chessboard.
#     - row (int): The queen's current row position.
#     - N (int): The number of queens.
#     - results (list): Matrix containing all the chessboards.
#     Returns:
#     - list: Updated results matrix.
#     """


#     # Base case: all queens are placed
#     if row == N:
#         # add the current solution to the results
#         results.append([[i, board[i]] for i in range(N)])
#         return
#     # Try placing a queen in each row of the current column
#     for col in range(N):
#         if is_safe(board, row, col):
#             board[row] = col
#             solve_puzzle(board, row + 1, N, results)


def is_safe(board, row, col):
    """
    Helper function that checks the board before placing a queen.
    Args:
    - board (list): The current working chessboard.
    - row (int): The queen last position on a row.
    - col (int): The queen last position on a col.
    Return:
    - True if it's safe to place the queen or False otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if (
            board[i] == col  # queen vertically in the same column
            or board[i] + i == col + row  # queen in the right diagonal
            or board[i] - i == col - row  # queen in the left diagonal
        ):
            return False
    return True


if __name__ == "__main__":
    main()
