# Description

Given an `m x n` binary matrix `mat`, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

## Topics

Array; Matrix; Dynamic Programming; Breadth-First Search

## Example 1

```
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
```

## Example 2

```
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
```

# Solution

Taken from [this solution](https://leetcode.com/problems/01-matrix/solutions/1369741/c-java-python-bfs-dp-solutions-with-picture-clean-concise-o-1-space/).

## Solution 1

The first solution involves BFS starting at the 0 nodes. This is pretty self-explanatory, with the clever trick being the `DIR` variable used. This is an $\mathcal{O}(MN)$ solution in both space and time.

```py
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        DIR = [0, 1, 0, -1, 0]

        q = deque([])
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1  # Marked as not processed yet!

        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1: continue
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))
        return mat
```

## Solution 2

The second solution is to use DP, and uses a 2-pass approach. First, we move from the top-left corner to the bottom-right; in the second pass, we move from the bottom-right corner to the top-left. 

```py
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    top = mat[i - 1][j] if i > 0 else math.inf
                    left = mat[i][j - 1] if j > 0 else math.inf
                    mat[i][j] = min(top, left) + 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] != 0:
                    bottom = mat[i + 1][j] if i < m - 1 else math.inf
                    right = mat[i][j + 1] if j < n - 1 else math.inf
                    mat[i][j] = min(mat[i][j], bottom + 1, right + 1)
        
        return mat
        
```
