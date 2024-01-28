# Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


## Example 1:

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

## Example 2:

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

# Solution

The brute-force solution is obvious. The better solution proceeds as follows: keep an index `i` of the best buy time, and an index `j` of the best sell time. Keep an intermediary buy index `ii`. You should think of `ii` as "the best buy time, but we do not know it yet". 

We now go over `prices`, and do the following: check the profit between the current price and the price at index `ii`; if it is higher than the profit we know, update the indices accordingly. If not, we check if we can update `ii`, which we do so by checking if the current price is lower than the price known at index `ii`. If so, we update it accordingly. The key here is you want to buy low and sell high, and `ii` tracks this. Lastly, we check if the profit from index `i` to `k` is higher than our max profit, and if so, update accordingly.

We do not really need `j` in this solution, but it's a good mental model of what's really happening.
