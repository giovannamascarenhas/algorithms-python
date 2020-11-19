def binary_search(input_array, value):
    meio = input_array[len(input_array) // 2]
    nova_lista = []
    index_meio = input_array.index(meio)
    if value == meio:
        return 1
    elif value > meio:
        nova_lista = input_array[index_meio+1::]
    else:
        nova_lista = input_array[0:index_meio]
    
    if nova_lista and len(nova_lista) > 1:
        while len(nova_lista) > 1:
            meio = nova_lista[len(nova_lista) // 2]
            index_meio = nova_lista.index(meio)
            if meio == value:
                return meio
                break
            if value > meio:
                nova_lista = nova_lista[index_meio+1::]
            else:
                nova_lista = nova_lista[0:index_meio]
            if len(nova_lista) == 1:
                if value in nova_lista:
                    return input_array.index(value)
                return -1
            break
    return -1   


def binary_search2(array, value):   
    start, mid = 0, 0
    high = len(array)
    while start <= high:
        mid = (start + high) // 2
        if value > array[mid]:
            start = mid + 1
        elif value < array[mid]:
            high = mid - 1
        else:
            return 1
    return -1
    


array = [1,3,9,11,15,19,29]
value = 29

print(binary_search2(array, value))
