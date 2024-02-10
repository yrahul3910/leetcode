# Description

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different `order`. The `order` of the alphabet is some permutation of lowercase letters.

Given a sequence of `words` written in the alien language, and the `order` of the alphabet, return `true` if and only if the given `words` are sorted lexicographically in this alien language.

## Topics

Array; Hash Table; String

## Example 1:

```
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
```

## Example 2:

```
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
```

## Example 3:

```
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character.
```

# Solution

There seem to be two primary approaches: one involving remapping the alien words so that they're ordered by the English language and then checking if they're sorted, and the other checking if they're sorted according to the alien alphabet. The solution here uses the latter approach.

First, we need a way to compare characters, which we do by building a HashMap. Next, we keep a pointer to the character we're currently looking at. We will proceed by removing words that are in the correct order; if they are not, we return immediately. If we're left with a single word, we're done. The rest of the solution is merely about incrementing the pointer, removing words, and returning appropriately.
