# Coin Change Calculator

This Python script contains a function `make_change` that calculates the minimum number of coins needed to meet a given total.

## Usage

### Function Signature:

```python
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
