# Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in $\mathcal{O}(\log_2 n)$ time and $\mathcal{O}(1)$ space.

## Topics

Array; Binary Search

## Example 1:

```
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
```

## Example 2:

```
Input: nums = [3,3,7,7,10,11,11]
Output: 10
```

# Solution

Since the array is sorted, we can use a binary search. Notice that at each iteration, if `mid` is odd, it need to be equal to the one before it; if it is even, it needs to be equal to the next element--if that is not true, we need to recurse accordingly, since that is where the error is.
