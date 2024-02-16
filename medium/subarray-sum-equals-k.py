# https://leetcode.com/problems/subarray-sum-equals-k/
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_freq = {}
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(nums[i] + sums[i - 1])
        
        count = 0
        for i, x in enumerate(sums):
            if x - k in sum_freq:
                count += sum_freq[x - k]
            if k == x:
                count += 1
            sum_freq[sums[i]] = sum_freq.get(sums[i], 0) + 1
        
        return count
