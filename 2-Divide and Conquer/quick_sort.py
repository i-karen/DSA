def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high - 1

    while (i < j):
        while (arr[i] <= pivot):
            i += 1
        while (arr[j] > pivot):
            j -= 1
        if (i < j):
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]

    return j


def quick_sort(arr, low, high):

    if (low < high):

        partition_index = partition(arr, low, high)

        quick_sort(arr, low, partition_index)
        quick_sort(arr, partition_index + 1, high)


arr = [7, 5, 4, 2, 9, 8, 6]
quick_sort(arr, 0, len(arr))
print("sorted array is {}".format(arr))