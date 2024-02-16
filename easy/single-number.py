# https://leetcode.com/problems/single-number/
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k = 0
        for x in nums:
            k ^= x
        
        return k
