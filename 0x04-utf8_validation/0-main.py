#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

# Valid UTF-8 sequences
#------------------------
data = [65]
print(validUTF8(data))
data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

print(validUTF8([0b0])) # Single byte character
print(validUTF8([0b11000010, 0b10000010])) # Two byte character
print(validUTF8([0b11100010, 0b10000010, 0b10000010])) # Three byte character
print(validUTF8([0b11110000, 0b10000010, 0b10000010, 0b10000010])) # Four byte character

# Invalid UTF-8 sequences
#--------------------------
data = [229, 65, 127, 256]
print(validUTF8(data))

print(validUTF8([0b10000000])) # Continuation byte as start of character
print(validUTF8([0b11000010])) # Missing continuation byte
print(validUTF8([0b11100010, 0b10000010])) # Missing continuation byte
print(validUTF8([0b11110000, 0b10000010, 0b10000010])) # Missing continuation byte
print(validUTF8([0b11000010, 0b11000010])) # Continuation byte does not start with 10
print(validUTF8([0b11100010, 0b11000010, 0b10000010])) # Continuation byte does not start with 10
print(validUTF8([0b11110000, 0b11000010, 0b10000010, 0b10000010])) # Continuation byte does not start with 10
