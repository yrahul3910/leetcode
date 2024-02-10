# Description

Given an `m x n` matrix `mat`, return an array of all the elements of the array in a diagonal order.

## Example 1:

![Image](https://assets.leetcode.com/uploads/2021/04/10/diag1-grid.jpg)

```
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
```

## Example 2:

```
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
```

## Topics

Array; Matrix

# Solution

You could adapt the solution from [Diagonal Traverse II](medium/diagonal-traverse-2.md) here, like so:

```
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        vals = []
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                vals.append((i + j, (-1) ** (i + j) * j, val))
        return [x[2] for x in sorted(vals)]
```

The problem here is that because this problem has a filled-out matrix, this becomes $\mathcal{O}(MN\log_2 MN)$ because of the last statement. An $\mathcal{O}(MN)$ solution just uses a HashMap from diagonal sums to the values in the diagonal.
