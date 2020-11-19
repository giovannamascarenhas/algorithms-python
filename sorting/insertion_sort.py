def insertion_sort(arr):
    for item in range(1, len(arr)):
        key_item = arr[item]
        sub_array = item - 1
        while sub_array >= 0 and arr[sub_array] > key_item:
            arr[sub_array + 1] = arr[sub_array]
            sub_array -= 1
        arr[sub_array + 1] = key_item
    return arr


array = [8,2,6,4,5]
