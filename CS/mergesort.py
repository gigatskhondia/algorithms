def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [None for _ in range(n1)]
    R = [None for _ in range(n2)]
    for i in range(n1):
        L[i] = arr[p + i]
    for j in range(n2):
        R[j] = arr[q + j + 1]

    i = 0
    j = 0

    for k in range(p, r):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
            if i == len(L):
                arr[k + 1:r + 1] = R[j:]
                break
        else:
            arr[k] = R[j]
            j += 1
            if j == len(R):
                arr[k + 1:r + 1] = L[i:]
                break


def merge_sort(arr, p, r):  # n*lg(n)
    if p < r:
        q = (p+r)//2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)
