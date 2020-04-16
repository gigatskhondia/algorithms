def min_index(arr):
    min_ = arr[0]
    index_ = 0
    for i in range(len(arr)):
        if arr[i] < min_:
            min_ = arr[i]
            index_ = i
    return index_


def selection_sort(arr):  # n**2
    for j in range(len(arr)-1):
        min_ind = min_index(arr[j:])+j
        if j != min_ind:
            arr[j], arr[min_ind] = arr[min_ind], arr[j]
    return arr
