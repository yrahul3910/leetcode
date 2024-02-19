# Description

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

## Topics

Array; Dynamic Programming

## Example 1:

```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

## Example 2:

```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
```

# Solution

It's tempting to think the result is the maximum of the odd sums and the even sums, which fails when there are larger gaps in between the houses of the optimal solution.

To understand why this problem qualifies for DP, note that if we removed $k$ elements from the right of the array, that would still be a valid subproblem. As such, there is a subproblem structure that we can exploit, making DP a candidate. Obviously, we'll create a 1D DP array where each element holds the solution to that subproblem (the array until that element). Notice that at each step, you could either skip the house (so that your reward is `dp[i - 1]`) or rob it (so that your reward is `dp[i - 2] + nums[i]`). At each iteration, we take the maximum of these.

