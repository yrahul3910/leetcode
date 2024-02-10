# https://leetcode.com/problems/verifying-an-alien-dictionary/
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {c: i for i, c in enumerate(order)}

        ptr = 0
        while True:
            if len(words) == 1:
                return True
            for i in range(len(words) - 1, 0, -1):
                if ptr >= len(words[i]):
                    if words[i-1] != words[i]:
                        return False
                    words.remove(words[i])
                elif ptr >= len(words[i-1]):
                    words.remove(words[i-1])
                elif order_dict[words[i][ptr]] > order_dict[words[i-1][ptr]]:
                    words.remove(words[i])
                elif order_dict[words[i][ptr]] < order_dict[words[i-1][ptr]]:
                    return False
                else:
                    ptr += 1

