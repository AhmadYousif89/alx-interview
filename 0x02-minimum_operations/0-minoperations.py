#!/usr/bin/python3
"""
Minimum Operations:
In a text file, there is a single character H.
Your can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
- Prototype: def minOperations(n): n must be an integer >= 2
- Returns an integer
- If n is impossible to achieve, return 0

Example:
>>> n = 6
>>> H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH
>>> Number of operations: 5
"""


def minOperations(n):
    if n < 2 or type(n) is not int or n is None:
        return 0

    operations = 0
    for i in range(2, n + 1):
        while n % i == 0:
            operations += i
            n = n / i

    return operations
