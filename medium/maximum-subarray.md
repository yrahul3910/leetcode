# Maximum Subarray

Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

## Topics

Array; Divide and Conquer; Dynamic Programming

## Example 1:

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
```

## Example 2:

```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
```

## Example 3:

```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
```

# Solution

This can be done using DP, but this is a classic introduction to divide-and-conquer. CLRS Chapter 4 covers this exact problem, but the key idea is the same: compute the maximum sum of the left and right halves, and the maximum sum of subarrays crossing the midpoint. The core of the solution is in computing this maximum crossing subarray. The key is to compute a "left sum" that goes from the midpoint to the left end, and a "right sum" that goes from the midpoint to the right, and a "middle sum" that includes both. The maximum sum is the maximum of the three of these.

# A better solution

The above is an $\mathcal{O}(n \log_2 n)$ solution, but the DP approach, called [Kadane's algorithm](https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm), is $\mathcal{O}(n)$ and simpler:

```py
def maxSubArray(nums):
    if not nums:
        return 0

    max_ending_here = max_so_far = nums[0]

    for num in nums[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
```

The key variable is `max_ending_here`, which maintains the maximum sum of any subarray that ends at index $j$. Because of the way it is calculated, it can "start" a new subarray without keeping one in memory (see the first line in the loop). Of course, there is also a variable keeping track of the overall maximum subarray sum.
