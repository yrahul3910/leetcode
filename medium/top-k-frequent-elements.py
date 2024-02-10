# https://leetcode.com/problems/top-k-frequent-elements/
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        max_freq = max(d.values())
        freq = [[] for _ in range(max_freq + 1)]
        for num, f in d.items():
            freq[f].append(num)
        
        result = []
        for i in range(max_freq, -1, -1):
            for num in freq[i]:
                result.append(num)

                if len(result) == k:
                    return result
        
