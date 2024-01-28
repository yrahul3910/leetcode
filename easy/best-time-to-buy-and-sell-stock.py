# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        # Brute force
        if len(prices) == 1:
            return 0

        profits = [max([x - price for price in prices[:i+1]]) for i, x in enumerate(prices[1:])]

        return max(max(profits), 0)
        """
        max_profit = 0
        i = 0
        ii = 0
        j = 0

        for k in range(1, len(prices)):
            if prices[k] - prices[ii] > max_profit:
                i = ii
                j = k
                max_profit = prices[k] - prices[ii]

            if prices[k] < prices[ii]:
                ii = k

            if prices[k] - prices[i] > max_profit:
                max_profit = prices[k] - prices[i]
                j = k
        
        return max_profit

        
