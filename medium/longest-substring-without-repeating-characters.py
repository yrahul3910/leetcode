# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        result = 0
        d = {}

        for right, c in enumerate(s):
            if c in d:
                left = max(d[c] + 1, left)
            
            d[c] = right
            result = max(result, right - left + 1)
        
        return result
