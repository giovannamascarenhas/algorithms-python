from random import randint


def quick_sort(array):
    if len(array) < 2:
        return array
    low = []
    high = []
    same = []
    pivo = array[randint(0, len(array) - 1)]

    for element in array:
        if element < pivo:
            low.append(element)
        elif element == pivo:
            same.append(element)
        else:
            high.append(element)
    return quick_sort(low) + same + quick_sort(high)


array = [8, 2, 6, 4, 5, 7]
