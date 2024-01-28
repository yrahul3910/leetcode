import math


class MaxHeap:
    items = []
    heap_size = 0

    def __getitem__(self, key):
        return self.items[key]
    
    def __setitem__(self, key, value):
        self.items[key] = value

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def parent(i):
    return math.floor((i - 1) / 2)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def max_heapify(arr: MaxHeap, i: int):
    """
    Assumes that the binary trees rooted at left(i) and right(i) are max heaps, but that A[i] might be smaller than
    its children, thus violating the max-heap property. max_heapify lets the value at A[i] "float down" in the max-heap
    so that the subtree rooted at index i obeys the max-heap property.

    T(n) <= 2T(2n/3) + O(1)
    T(n) = O(lg n)
    """
    l = left(i)
    r = right(i)

    if l < arr.heap_size and arr[l] > arr[i]:
        largest = l
    else:
        largest = i

    if r < arr.heap_size and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest)


def build_max_heap(arr: list):
    """
    Produces a max-heap from an unordered input array.

    T(n) = O(n)
    """
    heap = MaxHeap()
    heap.items = arr[:]
    heap.heap_size = len(arr)

    for i in range(math.floor(len(arr) / 2), -1, -1):
        max_heapify(heap, i)

    return heap


def heap_sort(arr):
    """
    Sorts an array.

    T(n) = O(n lg n)
    """
    heap = build_max_heap(arr)
    for i in range(len(heap) - 1, 0, -1):
        # Put the largest element in its place
        heap[0], heap[i] = heap[i], heap[0]

        # Now ignore the last element and repeat
        heap.heap_size -= 1
        max_heapify(heap, 0)

    return heap


if __name__ == "__main__":
    arr = [5, 3, 1, 4, 2, 6]
    print(heap_sort(arr))
