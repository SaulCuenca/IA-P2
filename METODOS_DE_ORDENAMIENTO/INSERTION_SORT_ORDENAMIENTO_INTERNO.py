def insertion_sort(arr):
    # Recorremos la lista desde el segundo elemento hasta el final.
    for i in range(1, len(arr)):
        # Almacenamos el elemento actual en una variable temporal.
        current_element = arr[i]
        # Comenzamos a comparar el elemento actual con los elementos anteriores.
        j = i - 1
        while j >= 0 and current_element < arr[j]:
            # Si el elemento actual es menor que el elemento en la posición j,
            # movemos el elemento en la posición j una posición hacia la derecha.
            arr[j + 1] = arr[j]
            j -= 1
        # Insertamos el elemento actual en su posición correcta.
        arr[j + 1] = current_element

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Lista original:", arr)
    insertion_sort(arr)
    print("Lista ordenada:", arr)
