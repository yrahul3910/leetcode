# https://leetcode.com/problems/house-robber/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        dp = nums[:2] + [0 for _ in range(len(nums) - 2)]
        dp[1] = max(dp[1], dp[0])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        
        return dp[-1]
