#!/usr/bin/python3
"""Validate UTF-8 encoding of a list of integers."""


def validUTF8(data):
    """
    Method that determines if a given data represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, False otherwise.
    """
    # Counter for the number of bytes in the current character
    n_bytes = 0
    # Masks to check if the most significant bit is set or not
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        # Get only the 8 least significant bits
        byte = num & 0xFF

        if n_bytes == 0:
            # Determine how many bytes the UTF-8 character has
            mask = 1 << 7
            while byte & mask:
                n_bytes += 1
                mask = mask >> 1

            # 1 byte characters
            if n_bytes == 0:
                continue

            # Invalid scenarios
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check if the byte is of the form 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        n_bytes -= 1

    return n_bytes == 0
