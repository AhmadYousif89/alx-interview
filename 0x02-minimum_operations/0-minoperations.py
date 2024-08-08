#!/usr/bin/python3
"""
Minimum Operations:
In a text file, there is a single character H.
You can execute only two operations in this file: Copy All and Paste.

This simple alogrithm will calculates the fewest number of operations
needed to result in exactly n.'H' characters in the file.

- Prototype: def minOperations(n: int) -> int:
- n must be an integer >= 2
- Returns n of operations or if n is impossible to achieve, return 0

Example:
>>> n = 6
>>> H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH
>>> Minimum number of operations: 5
"""


def minOperations(n):
    """Minimum Operations to reach n.'H' characters"""
    if not isinstance(n, int) or n <= 1:
        return 0

    operations = 0
    for i in range(2, n + 1):
        while n % i == 0:
            operations += i
            n //= i

    return operations
