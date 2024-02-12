N Queens Problem Solver

This project provides a Python script to solve the N Queens problem, which is the challenge of placing N non-attacking queens on an N×N chessboard.
Requirements

    Allowed editors: vi, vim, emacs
    All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
    Files should end with a new line
    The first line of all files should be exactly #!/usr/bin/python3
    PEP 8 style (version 1.7.*) should be followed
    All files must be executable

Usage

mathematica

./0-nqueens.py N

    Replace N with the size of the chessboard (an integer greater or equal to 4).
    If the user calls the program with the wrong number of arguments, it will print Usage: nqueens N and exit with status 1.
    If N is not an integer or smaller than 4, appropriate error messages will be printed.
    The program will print every possible solution to the problem, with one solution per line.

Example

lua

$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

css

$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]

Repository Information

    GitHub Repository: alx-interview
    Directory: 0x05-nqueens
    File: 0-nqueens.py