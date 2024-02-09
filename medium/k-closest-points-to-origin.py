# https://leetcode.com/problems/k-closest-points-to-origin
import math
from typing import List


class MinHeap:
    heap_size = 0
    items = []

    def __getitem__(self, idx):
        return self.items[idx]
    
    def __setitem__(self, k, v):
        self.items[k] = v
    
    def __repr__(self):
        return self.items.__repr__()

def parent(i):
    return math.floor((i - 1) // 2)

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def dist(x):
    return math.sqrt(x[0] ** 2 + x[1] ** 2)

def min_heapify(arr: MinHeap, i: int):
    _min = i
    _min_dist = dist(arr[_min])

    l = left(i)
    r = right(i)
    if l < arr.heap_size and dist(arr[l]) < _min_dist:
        _min = l
    if r < arr.heap_size and dist(arr[r]) < dist(arr[_min]):
        _min = r
    if _min != i:
        arr[i], arr[_min] = arr[_min], arr[i]
        min_heapify(arr, _min)

def build_min_heap(arr: list):
    heap = MinHeap()
    heap.items = arr[:]
    heap.heap_size = len(arr)

    for i in range(int(len(arr) // 2), -1, -1):
        min_heapify(heap, i)
    
    return heap

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:k]

        """
        # Heap solution
        heap = build_min_heap(points)

        for j in range(k):
            i = len(points) - j - 1
            heap[0], heap[i] = heap[i], heap[0]
            heap.heap_size -= 1
            min_heapify(heap, 0)
        
        print(heap)
        return heap[-k:]
        """
