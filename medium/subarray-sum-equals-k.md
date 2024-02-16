# Description

Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

## Topics

Array; Hash Table; Prefix Sum

## Example 1:

```
Input: nums = [1,1,1], k = 2
Output: 2
```

## Example 2:

```
Input: nums = [1,2,3], k = 3
Output: 2
```

# Solution

The key here is to note that `sum(i, j) = sum(0, j) - sum(0, i)`. As such, we first need to build a list of cumulative sums, along
with a frequency map. Next, we iterate over the cumulative sums, so that we are iterating over `sums(0, j)`. We look in the frequency 
map for `x - k`, where `x = sums(0, j)` and `k` is the target.
