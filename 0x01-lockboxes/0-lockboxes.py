#!/usr/bin/python3
"""
This file contains the canUnlockAll function that takes a list
(boxes: List[List[int]]) as argument and returns a boolean
to determine if all the boxes can be opened or not.
"""


def canUnlockAll(boxes):
    """Check if all boxes can be opened"""
    n = len(boxes)
    opened = set([0])
    keys = set(boxes[0])

    while keys:
        new_keys = set()
        for key in keys:
            if key < n and key not in opened:
                opened.add(key)
                new_keys.update(boxes[key])
        keys = new_keys

    return len(opened) == n
