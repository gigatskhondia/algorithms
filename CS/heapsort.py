def parent(i):
    return i//2


def left(i):
    return 2*i


def right(i):
    return 2*i + 1


def max_heapify(arr, i, heap_size):
    l = left(i)
    r = right(i)
    if l <= heap_size and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heap_size)


def build_max_heap(arr):
    heap_size = len(arr)-1
    for i in range(len(arr)//2, -1, -1):
        max_heapify(arr, i, heap_size)
    return arr, heap_size


def heap_sort(arr):  # n*lg(n)
    arr, heap_size = build_max_heap(arr)
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size = heap_size-1
        max_heapify(arr, 0, heap_size)
