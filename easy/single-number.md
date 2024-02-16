# Description

Given a non-empty array of integers `nums`, every element appears *twice* except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

## Topics

Array; Bit Manipulation

## Example 1:

```
Input: nums = [2,2,1]
Output: 1
```

## Example 2:

```
Input: nums = [4,1,2,1,2]
Output: 4
```

## Example 3:

```
Input: nums = [1]
Output: 1

```

# Solution

This is a standard introduction to XOR. Use the property that `a ^ a = 0` and `0 ^ a = a`.
