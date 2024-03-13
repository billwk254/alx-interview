#!/usr/bin/python3
"""
Determines the winner of the prime game.
"""


def is_prime(n):
    """
    Checks if a number is prime.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def calculate_primes(n):
    """
    Generates a list of prime numbers up to n.
    """
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def isWinner(x, nums):
    """
    Determines the winner of the prime game for each round.
    """
    winners = {"Maria": 0, "Ben": 0}

    for i in range(x):
        primes = calculate_primes(nums[i])
        if len(primes) % 2 == 0:
            winners["Ben"] += 1
        else:
            winners["Maria"] += 1

    if winners["Maria"] == winners["Ben"]:
        return None
    return max(winners, key=winners.get)


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
