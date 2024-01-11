#!/usr/bin/python3

"""
A python file to solve the lockboxes puzzle in python
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened
    """
    # Initialize a set to store the keys
    keys = set()
    # Add the first key (0) to the set
    keys.add(0)
    # Call the recursive helper function with the first box
    return unlock(boxes, 0, keys)


def unlock(boxes, box, keys):
    """
    Helper function that checks if a box can be opened
    """
    # Base case: if the box is empty, return True
    if not boxes[box]:
        return True
    # Loop through the keys in the box
    for key in boxes[box]:
        # If the key is valid and not already in the set
        if key < len(boxes) and key not in keys:
            # Add the key to the set
            keys.add(key)
            # Recursively check if the box with that key can be opened
            unlock(boxes, key, keys)
    # Return True if the size of the set is equal to the number of boxes
    return len(keys) == len(boxes)
