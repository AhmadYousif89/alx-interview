#!/usr/bin/python3
"""
Soulving the making change problem with minimum number of coins
"""


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
    if len(coins) == 0:
        return -1
    # Sort the coins for easy iteration
    coins.sort()
    # Initialize the dp array with infinity, and set the first element to 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for i in range(1, total + 1):
        for j in range(len(coins)):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
            else:
                break
    return dp[total] if dp[total] != float('inf') else -1


if __name__ == "__main__":
    print(makeChange([1, 2, 5], 11))  # output should be 3
    print(makeChange([1, 2, 25], 37))  # output should be 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # output should be -1
    print(makeChange([1, 2, 5], 0))  # output should be 0
    print(makeChange([], 1))  # output should be -1
