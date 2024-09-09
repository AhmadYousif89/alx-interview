#!/usr/bin/python3
"""
Implementation of a 2d matrix rotation in place by 90 degrees clockwise.

Example:
>>>    1 2 3      7 4 1
>>>    4 5 6  ->  8 5 2
>>>    7 8 9      9 6 3

Usage:
    ./0-rotate_2d_matrix.py or ./main.py
"""


def rotate_2d_matrix(mat):
    """
    Rotate a 2d matrix in place by 90 degrees

    Args :
    -   mat (List[List[Int]]): A 2d matrix of integers
    """
    if len(mat) == 0 or len(mat) != len(mat[0]) or len(mat[0]) == 0:
        return

    l, r = 0, len(mat) - 1

    while l < r:
        for i in range(r - l):
            topleft = mat[l][l + i]  # Save the top left element
            # Move the bottom left element to the top left
            mat[l][l + i] = mat[r - i][l]
            # Move the bottom right element to the bottom left
            mat[r - i][l] = mat[r][r - i]
            # Move the top right element to the bottom right
            mat[r][r - i] = mat[l + i][r]
            # Move the top left element to the top right
            mat[l + i][r] = topleft
        # Move to the next inner layer
        l += 1
        r -= 1


# Function to print the matrix
def displayMatrix(mat1, mat2):
    for i in range(0, len(mat1)):
        for j in range(0, len(mat1)):
            print('|', mat1[i][j], end=' ' if j < len(mat1) - 1 else ' |')
        print(' -> ', end='') if i == 1 else print('    ', end='')
        for j in range(0, len(mat2)):
            print('|', mat2[i][j], end=' ' if j < len(mat2) - 1 else ' |')
        print()


if __name__ == "__main__":
    rotated_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    original_mat = [row[:] for row in rotated_mat]
    rotate_2d_matrix(rotated_mat)
    displayMatrix(original_mat, rotated_mat)
