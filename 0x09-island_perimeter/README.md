# Island Perimeter

The goal is to calculate the perimeter of a single island in a grid, where the grid is represented by a 2D array of integers.

Understanding how to navigate and analyze 2D arrays and apply logical operations to determine the conditions for perimeter calculation is crucial for this task.

## Concepts

- **2D Arrays:**

  - Accessing and iterating over elements in a 2D array.
  - Understanding how to navigate through adjacent cells (horizontally and vertically).

- **Logical Operations:**

  - Using logical operators to determine conditions for calculating the perimeter of an island.

- **Counting Techniques:**

  - Developing a method to count the perimeter of an island based on the number of adjacent cells.

- **Problem-Solving Strategies:**

  - Analyzing the problem requirements and constraints to develop an effective solution.

- **Python Programming:**

  - Nested loops for iterating over grid cells.
  - Conditional statements to check the status of adjacent cells.

## Approach

To calculate the perimeter of an island in a grid, we can follow these steps:

1. Iterate over each cell in the grid.
2. Apply logical operations to determine if the cell is part of the island.
3. For each cell that is part of the island, check the adjacent cells to determine the number of sides exposed to water.
4. Calculate the perimeter based on the number of exposed sides for each cell.
5. Sum the perimeter values for all cells in the island to get the total perimeter.

By following this approach, we can efficiently calculate the perimeter of a single island in a grid.

## Example

Suppose we have a grid representing an island:

```
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
```

To calculate the perimeter of this island, we can iterate over each cell and apply the following logic:

- Assuming the cell value `1` represents land, and the cell value `0` represents water.
- For each land cell, check the adjacent cells to determine the number of exposed sides.
- Calculate the perimeter based on the number of exposed sides for each cell.

```python
def island_perimeter(grid):
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    return perimeter
```

Applying this logic to the given grid, we can calculate the perimeter of the island as follows:

- The perimeter of the island in the given grid is `16`.
