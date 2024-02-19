# https://leetcode.com/problems/min-cost-climbing-stairs/
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costs = [0, cost[0]] + cost[1:] + [0]

        for i in range(2, len(costs)):
            costs[i] = min(costs[i - 1], costs[i - 2]) + costs[i]
        
        return costs[-1]

