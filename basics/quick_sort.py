import random


def partition(arr: list, p: int, r: int) -> int:
    """
    Rearranges the subarray arr[p..r] in place

    T(n) = O(n)
    """
    x = arr[r]  # pivot
    i = p - 1

    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def randomized_partition(arr: list, p: int, r: int) -> int:
    """
    Rearranges the subarray arr[p..r] in place

    T(n) = O(n)
    """
    i = random.randint(p, r)
    arr[r], arr[i] = arr[i], arr[r]
    return partition(arr, p, r)


def quick_sort(arr: list, p: int, r: int):
    """
    Sorts an array.

    T(n) = O(n lg n)
    """
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)


def randomized_quicksort(arr: list, p: int, r: int):
    """
    Sorts an array.

    T(n) = O(n lg n)
    """
    if p < r:
        q = randomized_partition(arr, p, r)
        randomized_quicksort(arr, p, q - 1)
        randomized_quicksort(arr, q + 1, r)


if __name__ == "__main__":
    arr = [2, 8, 7, 1, 3, 5, 6, 4]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)

    arr = [2, 8, 7, 1, 3, 5, 6, 4]
    randomized_quicksort(arr, 0, len(arr) - 1)
    print(arr)
