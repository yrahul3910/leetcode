# https://leetcode.com/problems/single-element-in-a-sorted-array/
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]

        p = 0
        q = len(nums) - 1

        while p <= q:
            if q - p == 1:
                if p % 2 == 1 and nums[p] == nums[p - 1]:
                    return nums[q]
                return nums[p]
            
            mid = (p + q) // 2
            if mid % 2 == 1:
                if nums[mid] != nums[mid - 1]: 
                    q = mid
                else: 
                    p = mid
            elif mid % 2 == 0:
                if nums[mid] != nums[mid + 1]: 
                    q = mid
                else: 
                    p = mid
    
