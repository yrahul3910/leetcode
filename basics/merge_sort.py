def merge(left, right):
    arr = []

    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
           arr.append(left[i])
           i += 1
        else:
           arr.append(right[j])
           j += 1

    while i < len(left):
        arr.append(left[i])
        i += 1

    while j < len(right):
        arr.append(right[j])
        j += 1

    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    return merge(merge_sort(left), merge_sort(right))


if __name__ == "__main__":
    arr = [5, 3, 1, 4, 6, 7]
    print(merge_sort(arr))
