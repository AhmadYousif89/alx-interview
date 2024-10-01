#!/usr/bin/python3
"""Prime Game Challenge"""


def getPrimeNumbers(n):
    """Get all prime numbers up to (n)"""
    plength = n + 1
    primes = [True for _ in range(plength)]

    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, plength, p):
                primes[i] = False
        p += 1

    prime_numbers = [p for p in range(2, plength) if primes[p]]
    return prime_numbers


def playGame(n):
    """Simulate a single round of the game with (n) numbers"""
    primes = getPrimeNumbers(n)
    remaining_numbers = [True] * (n + 1)  # Track available numbers
    turn = 0  # 0 = Maria's turn, 1 = Ben's turn

    while primes:
        # The current player picks the first available prime
        prime = primes[0]
        # Remove the prime and all its multiples
        for i in range(prime, n + 1, prime):
            remaining_numbers[i] = False
        # Update primes by filtering out unavailable numbers
        primes = [p for p in primes if remaining_numbers[p]]
        # Switch turns
        turn = 1 - turn

    # If the game ended on Maria's turn, Ben wins, and vice versa
    return 'Maria' if turn == 1 else 'Ben'


def isWinner(x, nums):
    """
    Determine the winner of the prime game challenge

    Args :
        - x (int): the number of rounds
        - nums (list): the list of (n) for each round

    Returns :
        - the name of the player that won the most rounds
        - if the winner cannot be determined, return None
    """
    if x < 1 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = playGame(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return 'Maria'
    if ben_wins > maria_wins:
        return 'Ben'
    return None


if __name__ == '__main__':
    print("Prime Game Challenge")
    print("Winner: {}".format(isWinner(0, [])))  # None
    print("Winner: {}".format(isWinner(1, [1])))  # None
    print("Winner: {}".format(isWinner(1, [2])))  # win Maria
    print("Winner: {}".format(isWinner(1, [3])))  # win Ben
    print("Winner: {}".format(isWinner(2, [1, 2])))  # win Maria
    print("Winner: {}".format(isWinner(2, [2, 3])))  # win Ben
    print("Winner: {}".format(isWinner(3, [1, 4, 7])))  # win Ben
    print("Winner: {}".format(isWinner(3, [2, 3, 5])))  # win Maria
    print("Winner: {}".format(isWinner(3, [1, 1, 1])))  # win Ben
    print("Winner: {}".format(isWinner(3, [2, 2, 2])))  # win Maria
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))  # win Ben
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3, 6])))  # None
