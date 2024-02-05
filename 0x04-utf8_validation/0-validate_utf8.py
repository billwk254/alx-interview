#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Checks if the given data set is a valid UTF-8 encoding
    """
    num_bytes = 0

    for byte in data:
        byte = byte & 0xFF
        if num_bytes == 0:
            if byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            elif byte >> 7 == 0b0:
                continue
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
