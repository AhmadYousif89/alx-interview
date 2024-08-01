# Lockboxes Challenge

This project contains a Python function `canUnlockAll` that determines if all boxes in a given list of lists can be opened. Each box is numbered sequentially from `0` to `n-1` and may contain keys to other boxes. The first box (`boxes[0]`) is always unlocked.

## Algorithm

The algorithm uses a Breadth-First Search (BFS) approach to traverse through the boxes and collect keys. Here's a step-by-step explanation:

1. **Initialization**:

   - Create a set `opened` to keep track of which boxes have been opened, starting with the first box (`0`).
   - Create a set `keys` containing the keys found in the first box.

2. **Traversal**:

   - While there are keys in the `keys` set:
     - Create a new set `new_keys` to store keys found in the current iteration.
     - For each key in the `keys` set:
       - If the key corresponds to a box that hasn't been opened yet, add it to the `opened` set and update `new_keys` with the keys found in that box.
     - Update `keys` with `new_keys` for the next iteration.

3. **Check**:
   - After traversing all possible boxes, check if the number of opened boxes is equal to `n`.

## Function Prototype

```python
def canUnlockAll(boxes):
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
```

## Big O Notation

The time complexity of the canUnlockAll function is O(n + k), where:

n is the number of boxes.

k is the total number of keys across all boxes.

The space complexity is O(n) since we are using a list of size n to keep track of the opened boxes.

### Eaxmples

```python
>>> canUnlockAll = __import__('0-lockboxes').canUnlockAll
>>> boxes = [[1], [2], [3], [4], []]
>>> print(canUnlockAll(boxes))
True
>>> boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
>>> print(canUnlockAll(boxes))
True
>>> boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
>>> print(canUnlockAll(boxes))
False
```

### Conclusion

This algorithm efficiently determines if all boxes can be opened using a BFS approach, ensuring that all reachable boxes are unlocked and their keys are utilized.
