#!/usr/bin/python3

"""
This script contains a function for making change.

The make_change function calculates the minimum number of coins

Args:
    coins (list of int): The denominations of available coins.
    total (int): The total amount for which change needs to be made.

Returns:
    int: The fewest number of coins needed to meet the total.
         Returns 0 if the total is 0 or less.
         Returns -1 if the total cannot
"""


def make_change(coins, total):
    """
    Calculates the fewest number of coins needed to meet the total.

    Args:
        coins (list of int): The denominations of available coins.
        total (int): The total amount for which change needs to be made.

    Returns:
        int: The fewest number of coins needed to meet the total.
             Returns 0 if the total is 0 or less.
             Returns -1 if the total cannot be met by any combination of coins.
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if total == 0:
            return change
    return -1
