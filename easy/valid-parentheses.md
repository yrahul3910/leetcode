# Description

Given a string s containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Topics

String; Stack

## Example 1:

```
Input: s = "()"
Output: true
```

## Example 2:

```
Input: s = "()[]{}"
Output: true
```

## Example 3:

```
Input: s = "(]"
Output: false
```

# Solution

This is the standard introduction to stacks. When you see an opening bracket, you push it to the stack. When you see a closing one, you ensure the top is what you expect, and if so, pop it.
