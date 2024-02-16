# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        top = 0

        for c in s:
            if c == '(':
                top += 1
            else:
                if top == 0:
                    count += 1
                else:
                    top -= 1
        
        return abs(top) + count
