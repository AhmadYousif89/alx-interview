#!/usr/bin/python3
"""
Parse logs from stdin and print stats
Example of log line:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status_code> <file_size>

Prints:
File size: <total_size>
<status_code>: <number_of_calls>
"""

import sys


def log_stats(file_size, status_codes):
    """
    Print log stats
    """
    print("File size: {:d}".format(file_size))
    for k, v in status_codes.items():
        if v:
            print("{:d}: {:d}".format(k, v))


if __name__ == '__main__':
    file_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0,
    }
    try:
        for i, line in enumerate(sys.stdin, 1):
            try:
                parts = line.split()
                file_size += int(parts[-1])
                status_codes[int(parts[-2])] += 1
                if i % 10 == 0:
                    log_stats(file_size, status_codes)
            except Exception as e:
                pass
    except KeyboardInterrupt:
        pass
    finally:
        log_stats(file_size, status_codes)
