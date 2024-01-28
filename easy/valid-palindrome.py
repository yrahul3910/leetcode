class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = [c.lower() for c in s if c.isalnum()]
        return s1 == s1[::-1]

