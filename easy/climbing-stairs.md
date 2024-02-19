# Description

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## Topics

Math; Dynamic Programming; Memoization

## Example 1:

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

## Example 2:

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

# Solution

This is actually the Fibonacci series in disguise. To understand why, we first note that to reach the last step, your previous step was either $n - 1$ or $n - 2$. The key is that this is an OR operation, not an AND. This results in us adding the last two numbers. 

Having understood this, you can implement the Fibonacci series in any way--recursion is the slowest, DP is the next best but uses $\mathcal{O}(n)$ space, and the next best is to use two variables:

```
class Solution:
    def climbStairs(self, n: int) -> int:
        n1, n2 = 0, 1

        for i in range(1, n + 1):
            n1, n2 = n2, n1 + n2
        
        return n2
```

You could be fancy and prove the Fibonacci numbers have a closed-form solution and use that, too.

