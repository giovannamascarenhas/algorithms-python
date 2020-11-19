def bubble_sorting(array):
    array_lenght = len(array)
    for element in range(array_lenght):
        already_sort = True
        for item in range(array_lenght - element - 1):
            if array[item] > array[item + 1]:
                array[item], array[item + 1] = array[item + 1], array[item]
                already_sort = False
        if already_sort:
            break
    return array


array = [8,2,6,4,5]

