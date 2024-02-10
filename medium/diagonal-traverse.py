# https://leetcode.com/problems/diagonal-traverse/
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diags = {}
        for i, row in enumerate(mat):
            for j, val in enumerate(row):
                if i + j not in diags:
                    diags[i + j] = [val]
                else:
                    diags[i + j].append(val)

        result = []
        for d_sum, vals in diags.items():
            if d_sum % 2 == 0:
                result.extend(vals[::-1])
            else:
                result.extend(vals)
        
        return result
