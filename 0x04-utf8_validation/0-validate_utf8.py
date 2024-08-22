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

    num_bytes = 0  # Counter for the number of bytes in the current character
    mask1 = 1 << 7  # Mask to check the most significant bit (10000000)
    mask2 = 1 << 6  # Mask to check the second most significant bit (01000000)

    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Determine the number of bytes for the current character
            while byte & mask:
                num_bytes += 1
                mask >>= 1
            if num_bytes == 0:
                continue  # Single byte character (0xxxxxxx)
            # Invalid scenarios: 1-byte character or more than 4 bytes
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the byte starts with '10xxxxxx' for continuation bytes
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1  # Decrement the byte counter

    # All bytes should be accounted for in complete characters
    return num_bytes == 0
