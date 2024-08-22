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
    remaining_bytes = 0
    # Mask to check the most significant bit (10000000)
    first_bit_mask = 1 << 7
    # Mask to check the second most significant bit (01000000)
    second_bit_mask = 1 << 6

    for current_byte in data:
        current_bit_mask = 1 << 7
        if remaining_bytes == 0:
            # Determine the number of bytes for the current character
            while current_byte & current_bit_mask:
                remaining_bytes += 1
                current_bit_mask >>= 1
            if remaining_bytes == 0:
                continue  # Single byte character (0xxxxxxx)
            # Invalid scenarios: 1-byte character or more than 4 bytes
            if remaining_bytes == 1 or remaining_bytes > 4:
                return False
        else:
            # If we're expecting more bytes, they must start with '10' in 'b'
            if not (
                current_byte & first_bit_mask
                and not (current_byte & second_bit_mask)
            ):
                return False
        # After checking a byte, we expect one less byte in the character
        remaining_bytes -= 1

    # If we've correctly processed all bytes, num_bytes should be 0
    return remaining_bytes == 0
