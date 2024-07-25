# Pascal Triangle Algorithm

<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" alt="Pascal Triangle">
</div>

A pascal's triangle is an arrangement of numbers in a triangular array such that the numbers at the end of each row are 1 and the remaining numbers are the sum of the nearest two numbers in the above row. This concept is used widely in probability, combinatorics, and algebra. Pascal's triangle is used to find the likelihood of the outcome of the toss of a coin, coefficients of binomial expansions in probability, etc.

## Pascal's Triangle Formula

The formula to fill the number in the nth column and mth row of Pascal's triangle we use the Pascals triangle formula. The formula requires the knowledge of the elements in the (n-1)th row, and (m-1)th and nth columns. The formula is as follows:

```
nCm = n-1Cm-1 + n-1Cm
```

Where `n` is the row number and `m` is the position in the row. The first row is considered as row 0 and the first position in the row is considered as position 0.

Example: To find the 3rd element in the 4th row, we use the formula as follows:

```
4C2 = 4-1C2-1 + 4-1C2
⇒ 4C2 = 3C1 + 3C2
⇒ 4C2 = 3 + 3
⇒ 4C2 = 6
```

### Pascal's Triangle in Python

The following Python code generates Pascal's triangle up to a given number of rows:

```python
def pascals_triangle(rows):
    triangle = []
    for row in range(rows):
        triangle.append([1] * (row + 1))
        for col in range(1, row):
            triangle[row][col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
    return triangle


def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

print_triangle(pascal_triangle(5))
```

This code generates the following output:

```
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

### Important Notes on Pascal's Triangle:

- The sum of the numbers in each row of Pascal's triangle is equal to 2 raised to the power of the row number.
- The elements in the Pascals triangle can find out by finding the sum of the two adjoint elements in the preceding row.
- The elements in the Pascal's triangle are also used to find the coefficients of the binomial expansion of a given expression.
- The Pascal's triangle is named after the French mathematician Blaise Pascal.
