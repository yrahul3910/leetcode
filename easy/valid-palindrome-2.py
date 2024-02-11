# https://leetcode.com/problems/valid-palindrome-ii/
class Solution:
    def validPalindrome(self, s: str, err: int = 0) -> bool:
        i = 0
        j = len(s) - 1

        while i < j and i < len(s):
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif err == 0:
                err = 1
                if s[i] == s[j-1] and s[i+1] == s[j]:
                    return self.validPalindrome(s[i:j], 1) or self.validPalindrome(s[i+1:j+1], 1)
                if s[i] == s[j-1]:
                    j -= 1
                elif s[i+1] == s[j]:
                    i += 1
            else:
                return False

        return True

