# Description

You are given an integer array `cost` where `cost[i]` is the cost of `i`th step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

## Topics

Array; Dynamic Programming

## Example 1:

```
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
```

## Example 2:

```
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
```

# Solution

This is best visualized the way it's described in the problem. Concretely, it is of cost 0 to not do anything at the ground floor. Likewise, once you've reached the top floor, you're done, so the cost at the top floor is 0. As such, we will append 0 to the beginning and the end of the list. Now, starting at the second stair, we need to build a DP table (notice that for the first stair, this is already done). The recursion here is:

```
dp[i] = min(dp[i - 1], dp[i - 2]) + dp[i]
```

