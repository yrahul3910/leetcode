# Description

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]` represent the start and the end of the `i`th interval and `intervals` is sorted in ascending order by `start_i`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

## Topics

Array

## Example 1:

```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

## Example 2:

```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

# Solution

There are better ways to do this than the implementation here, but the core idea is the same: iterate over the intervals; if the new interval is completely outside, then insert the current interval and move on; otherwise, find the overlapping interval and merge.

The tricky part is really just the amount of housekeeping needed. You have cases where the original intervals is empty, or if the new interval is at the beginning or the end, and so on, but the core idea is really the same. We go over all the intervals from the current one onward until we find a case where we should not merge. At this point, we keep a record `n` of the end of the merged interval and break. However, you could run into a case where the end of the new interval is right in between two of the intervals, at which point you'll find that `n` is not set: here, set `n` to the end of the new interval (L31-33). There's also nuance about whether we include the last interval you looked at or the next one, but again, that's just housekeeping.

# A better solution, courtesy of ChatGPT

Here's a more elegant version:

```py
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        # Early exit for empty intervals
        if not intervals:
            return [newInterval]

        # Merge overlapping intervals
        merged_interval = newInterval
        for interval in intervals:
            if interval[1] < merged_interval[0]:
                result.append(interval)
            elif interval[0] > merged_interval[1]:
                result.append(merged_interval)
                merged_interval = interval
            else:
                merged_interval[0] = min(merged_interval[0], interval[0])
                merged_interval[1] = max(merged_interval[1], interval[1])

        result.append(merged_interval)
        return result
```

The crux is in the three cases. The first case checks if the current interval is entirely to the left of the `merged_interval`, in which case we simply add the current interval. The second case checks if the current interval is entirely to the right of the `merged_interval`, in which case merging is complete. The last case handles overlapping intervals by adjusting the `merged_interval` to encompass both itself and the current interval.

