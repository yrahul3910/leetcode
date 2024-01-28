# https://leetcode.com/problems/insert-interval/
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        if len(intervals) == 0:
            return [newInterval]

        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals

        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0] or newInterval[0] > interval[1]:
                # Entirely outside
                result.append(interval)
            elif newInterval[1] >= interval[0] and newInterval[0] <= interval[1]:
                inc = 0
                n = None
                for j in range(i, len(intervals)):
                    if newInterval[1] >= intervals[j][0] and newInterval[1] <= intervals[j][1]:
                        n = max(newInterval[1], intervals[j][1])
                        inc = 1
                        break
                    elif newInterval[1] < intervals[j][0]:
                        n = newInterval[1]
                        break

                if n is None:
                    inc = 1
                    n = newInterval[1]

                result.append([min(interval[0], newInterval[0]), n])
                result.extend(intervals[j+inc:])
                return result
        
        result.append(newInterval)
        return sorted(result)
