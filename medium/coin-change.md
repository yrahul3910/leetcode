# Description

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

## Topics

Array; Dynamic Programming; Breadth-First Search

## Example 1:

```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

## Example 2:

```
Input: coins = [2], amount = 3
Output: -1
```

## Example 3:

```
Input: coins = [1], amount = 0
Output: 0
```

# Solution

This is a 1D DP problem. The key is the recursion:

```
dp[i] = min(dp[i], dp[i - coin] + 1)
```

We need to build the `dp` array from 0 to `amount`.
