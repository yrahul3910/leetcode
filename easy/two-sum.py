from typing import List


# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {x: i for i, x in enumerate(nums)}
        
        for i, num in enumerate(nums):
            if target - num in map and i != map[target - num]:
                return [i, map[target - num]]
        
