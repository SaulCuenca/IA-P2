def quick_sort(arr):
    # Comprobamos si la lista está vacía o contiene un solo elemento.
    if len(arr) <= 1:
        return arr

    # Elegimos un elemento como pivote (en este caso, el último elemento de la lista).
    pivot = arr[-1]
    
    # Inicializamos listas para los elementos menores y mayores que el pivote.
    lesser = []
    greater = []
    
    # Recorremos la lista, excepto el pivote.
    for element in arr[:-1]:
        if element <= pivot:
            # Si el elemento es menor o igual al pivote, lo añadimos a la lista lesser.
            lesser.append(element)
        else:
            # Si el elemento es mayor que el pivote, lo añadimos a la lista greater.
            greater.append(element)
    
    # Llamamos recursivamente a quick_sort en las listas lesser y greater.
    # Concatenamos las tres partes para obtener la lista ordenada.
    return quick_sort(lesser) + [pivot] + quick_sort(greater)

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [12, 4, 5, 6, 7, 3, 1, 15]
    print("Lista original:", arr)
    sorted_arr = quick_sort(arr)
    print("Lista ordenada:", sorted_arr)

