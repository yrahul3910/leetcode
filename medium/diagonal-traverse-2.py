# https://leetcode.com/problems/diagonal-traverse-ii/
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        vals = []
        for i, row in enumerate(nums):
            for j, val in enumerate(row):
                vals.append((i + j, -i, val))
        
        return [x[2] for x in sorted(vals)]
