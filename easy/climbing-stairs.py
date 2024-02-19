# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        s5 = math.sqrt(5)
        return int((((1 + s5) / 2) ** (n + 1) - ((1 - s5) / 2) ** n + 1) / s5)

