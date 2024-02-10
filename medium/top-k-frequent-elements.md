# Description

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

## Topics

Array; Hash Table; Divide and Conquer; Sorting; Heap/Priority Queue; Bucket Sort; Counting; Quickselect

## Example 1:

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

## Example 2

```
Input: nums = [1], k = 1
Output: [1]
```

# Solution

The $\mathcal{O}(n \log_2 n)$ solution is obvious enough--create a HashMap of elements to frequencies, and sort the dictionary items.

However, there is a linear solution to this, and is based on bucket sort.

