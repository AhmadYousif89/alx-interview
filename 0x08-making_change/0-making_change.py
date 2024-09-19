#!/usr/bin/python3
"""
Soulving the making change problem with minimum number of coins
"""

from collections import deque


def makeChange(coins, total):
    """
    Given a target amount (total) and array (coins) of distinct coin values
    what's the fewest coins needed to make the change amount.

    Args :
    -   coins (list[int]) : array of coins
    -   total (int) : target amount

    Returns :
    -   int : minimum number of coins needed to make the change amount
    """

    if total <= 0:
        return 0

    # Queue for BFS, storing (current_total, number_of_coins_used)
    queue = deque([(0, 0)])
    # Set to track visited amounts to avoid redundant work
    visited = set([0])

    while queue:
        current_total, num_coins = queue.popleft()
        # Try each coin to see what total we can reach
        for coin in coins:
            next_total = current_total + coin
            # If we hit the target total, return the number of coins used
            if next_total == total:
                return num_coins + 1
            # If next total is valid and hasn't been visited, add to queue
            if next_total < total and next_total not in visited:
                visited.add(next_total)
                queue.append((next_total, num_coins + 1))
    # If we exhaust the queue without finding the exact total, return -1
    return -1


if __name__ == "__main__":
    print(makeChange([1, 2, 5], 11))  # output should be 3
    print(makeChange([1, 2, 25], 37))  # output should be 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # output should be -1
    print(makeChange([1, 2, 5], 0))  # output should be 0
    print(makeChange([], 1))  # output should be -1
