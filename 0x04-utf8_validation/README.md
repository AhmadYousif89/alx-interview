# UTF-8 Validation

UTF-8 is a variable-width character encoding used for electronic communication. It can encode all 1,112,064 valid Unicode code points using one to four 8-bit bytes. This README explains the UTF-8 encoding rules and provides a Python implementation for validating UTF-8 encoded data.

## UTF-8 Encoding Rules

In UTF-8, characters can be encoded using 1 to 4 bytes, following these rules:

1. For 1-byte characters:

   - The first bit is 0, followed by its Unicode code.

2. For n-byte characters (where n > 1):
   - The first n bits are all 1's.
   - The (n+1)th bit is 0.
   - Followed by (n-1) bytes, each starting with 10.

## UTF-8 Encoding Table

| Character number range (hexadecimal) | UTF-8 octet sequence (binary)       |
| ------------------------------------ | ----------------------------------- |
| 0000 0000 - 0000 007F                | 0xxxxxxx                            |
| 0000 0080 - 0000 07FF                | 110xxxxx 10xxxxxx                   |
| 0000 0800 - 0000 FFFF                | 1110xxxx 10xxxxxx 10xxxxxx          |
| 0001 0000 - 0010 FFFF                | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx |

## Implementation Notes

- The input for the UTF-8 validation function is an array of integers.
- Only the least significant 8 bits of each integer are used to store the data.
- Each integer represents exactly 1 byte of data.

## Python Implementation

def validUTF8(data): # Number of bytes in the current UTF-8 character
n_bytes = 0

```py
    # Mask to check if the most significant bit is set or not
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
```

# Example usage

```py
print(validUTF8([229, 65, 127, 256])) # False
```

## Examples

1. Valid UTF-8 encoding:

```py

   data = [197, 130, 1]

   # Represents the octet sequence: 11000101 10000010 00000001

   print(validUTF8(data)) # Output: True
```

2. Invalid UTF-8 encoding:

```py

   data = [229, 65, 127, 256]
   print(validUTF8(data)) # Output: False
```

<br>

## Conclusion

This implementation efficiently validates whether a given array of integers represents a valid UTF-8 encoding. It checks for proper byte sequences and handles edge cases as per the UTF-8 specification.
