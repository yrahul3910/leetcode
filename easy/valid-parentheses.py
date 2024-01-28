# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        PARENS = {
            '{': '}',
            '(': ')',
            '[': ']'
        }

        stack = []
        for c in s:
            if c in PARENS:
                stack.append(c)
            else:
                if PARENS[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        
        return True
        
