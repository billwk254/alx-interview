Lockboxes
This project contains a Python script that solves the lockboxes problem.

Problem description
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
Solution
The solution is based on using recursion and sets to keep track of the keys and boxes that can be opened. The main function canUnlockAll(boxes) initializes a set to store the keys and calls a helper function unlock(boxes, box, keys) with the first box. The helper function checks if a box can be opened and adds new keys to the set. It then recursively calls itself with the new keys until all possible boxes are checked. The main function returns True if the size of the set is equal to the number of boxes, else False.

Usage
To run the script, use the following command:

./0-lockboxes.py

To test the script, use the following command:

python3 -m doctest -v ./0-lockboxes.py