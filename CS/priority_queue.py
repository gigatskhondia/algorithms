from heapsort import max_heapify

def heap_maximum(arr):  # constant time
    return arr[0]


def heap_extract_max(arr, heap_size):  # lg(n)
    if heap_size<1:
        return "heap underflow"
    max_ = arr[0]
    arr[0] = arr[heap_size]
    heap_size -= 1
    max_heapify(arr, 0, heap_size)
    return max_
