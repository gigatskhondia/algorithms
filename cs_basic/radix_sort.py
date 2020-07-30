# A function to do counting sort of arr[] according to
# the digit represented by exp.


def counting_sort(array, exp1):
    n = len(array)

    # The output array elements that will have sorted arr
    output = [0] * n

    # initialize count array as 0
    count = [0] * 10

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = array[i] // exp1
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = array[i] // exp1
        output[count[index % 10] - 1] = array[i]

        count[index % 10] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers

    for i in range(len(array)):
        array[i] = output[i]


# Method to do Radix Sort


def radix_sort(array):
    # Find the maximum number to know number of digits
    max1 = max(array)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 // exp > 0:
        counting_sort(array, exp)
        exp *= 10


if __name__ == "__main__":
    # Driver code to test above
    arr = [0, 170, 45, 75, 90, 802, 24, 2, 66]
    radix_sort(arr)
    print(arr)
