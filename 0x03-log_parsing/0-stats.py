#!/usr/bin/python3
"""
Print the file size and number of lines for each status code.
"""

import sys
import signal


def print_stats(total_size, status_codes):
    """
    Print the file size and number of lines for each status code.

    Args:
        total_size (int): Total file size.
        status_codes (dict): Dictionary containing status codes and their counts.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    print_stats(total_size, status_codes)
    sys.exit(0)


def parse_line(line):
     """
    Signal handler function to print stats and exit gracefully on CTRL + C.

    Args:
        sig: Signal number.
        frame: Current stack frame.
    """
    try:
        parts = line.split()
        ip = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return ip, status_code, file_size
    except (ValueError, IndexError):
        return None


total_size = 0
status_codes = {}


signal.signal(signal.SIGINT, signal_handler)

try:
    for i, line in enumerate(sys.stdin, 1):
        parsed_line = parse_line(line)
        if parsed_line:
            ip, code, size = parsed_line
            total_size += size
            if code in [200, 301, 400, 401, 403, 404, 405, 500]:
                status_codes[code] = status_codes.get(code, 0) + 1

            if i % 10 == 0:
                print_stats(total_size, status_codes)
except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise
