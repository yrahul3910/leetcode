# Description

Given a string `s`, find the length of the longest substring without repeating characters.

## Topics

Hash Table; String; Sliding Window

## Example 1:

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

## Example 2:

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

## Example 3:

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
```

## Solution

This is another sliding window problem. You can do this using a HashSet structure, like so:

```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        result = 0

        for right, c in enumerate(s):
            while c in char_set:  # Shrink the window until there are no repeats
                char_set.remove(s[left])
                left += 1

            char_set.add(c)  # Add current character, expand the window 
            result = max(result, right - left + 1)  # Update longest substring length

        return result 
```

This is still actually $\mathcal{O}(n)$, since each character is visited at most twice. The key idea is that even if `left..right` is not the correct answer, the `result` variable keeps track of it, with the hope of expanding back if a longer substring arises. We want to give up quickly: for example, in the string `dvdf`, once we reach the second `d`, we move the indices to `vd` instead of `dv`, even though they are of equal length.

With some clever math, you can also get rid of the inner loop, though:

```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        result = 0
        d = {}

        for right, c in enumerate(s):
            if c in d:
                left = max(d[c] + 1, left)
            
            d[c] = right
            result = max(result, right - left + 1)
        
        return result
```
