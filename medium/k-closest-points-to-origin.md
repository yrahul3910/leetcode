# Description

Given an array of `points` where `points[i] = [x_i, y_i]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points on the X-Y plane is the Euclidean distance (i.e., $\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

## Topics

Array; Math; Divide and Conquer; Geometry; Sorting; Heap/Priority Queue; Quickselect

# Solution

You could just use 

```
return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:k]
```

which beats 99.37% of Python 3 solutions, but if you did want to write this yourself, it's a simple modification of heap-sort.
