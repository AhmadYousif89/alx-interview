#!/usr/bin/python3
"""
Implement the Pascal’s triangle algorithm
"""


def pascal_triangle(n):
    triangle = []
    for row in range(n):
        triangle.append([1] * (row + 1))
        for col in range(1, row):
            triangle[row][col] = (
                triangle[row - 1][col - 1] + triangle[row - 1][col]
            )
    return triangle
