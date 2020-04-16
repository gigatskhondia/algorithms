from CS.heapsort import max_heapify, parent


def heap_maximum(arr):  # constant time
    return arr[0]


def heap_extract_max(arr, heap_size):  # lg(n)
    if heap_size < 1:
        return "heap underflow"
    max_ = arr[0]
    arr[0] = arr[heap_size]
    heap_size -= 1
    max_heapify(arr, 0, heap_size)
    return max_


def heap_increase_key(arr, i, key):  # lg(n)
    if key < arr[i]:
        return "new key is smaller than current key"
    arr[i] = key
    while i > 0 and arr[parent(i)] < arr[i]:
        arr[i], arr[parent(i)] = arr[parent(i)], arr[i]
        i = parent(i)
