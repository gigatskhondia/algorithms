def binary_search(arr, s):  # lg(n)
    while True:
        ind = len(arr) // 2
        if len(arr) == 1 and arr[ind] != s:
            print("The number is not in the array!")
            return None

        if arr[ind] > s:
            arr = arr[:ind]
        elif arr[ind] < s:
            arr = arr[ind:]
        elif arr[ind] == s:
            return "Success!"
