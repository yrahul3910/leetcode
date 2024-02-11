# Description

Given a string `s`, return `true` if the `s` can be palindrome after deleting at most one character from it.

## Topics

Two Pointers; String; Greedy

## Example 1:

```
Input: s = "aba"
Output: true
```

## Example 2:

```
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
```

## Example 3:

```
Input: s = "abc"
Output: false
```

# Solution

This is pretty simple. Since we permit only one error, we keep track of whether we have an error yet or not. If we hit a mismatch with no errors so far, we need to check whether the left character or the right one needs to be removed. There is a test case where both ways look good but only one of them is correct, so we use recursion. A lot of other solutions use a separate `isPalindrome` function like below.

```java
class Solution {
    public boolean validPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                // Try skipping the character on the left
                if (isPalindrome(s, left + 1, right)) {
                    return true;
                }
                // Try skipping the character on the right
                if (isPalindrome(s, left, right - 1)) {
                    return true;
                }
                // If neither case is a palindrome, return false
                return false;
            }
            left++;
            right--;
        }

        return true;
    }

    private boolean isPalindrome(String s, int start, int end) {
        while (start < end) {
            if (s.charAt(start) != s.charAt(end)) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
}
```
