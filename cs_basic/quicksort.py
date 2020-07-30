def partition(arr, p, r):
    x = arr[r]
    i = p-1
    for j in range(p,r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1


def quick_sort(arr, p, r):  # n*lg(n) on average, but n**2 worst
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q-1)
        quick_sort(arr, q+1, r)
