def bubble_sort(arr):
    n = len(arr)
    
    # Iteramos a través de todos los elementos en la lista.
    for i in range(n):
        # La última i-ésima posición ya está en su lugar, así que no es necesario compararla de nuevo.
        # Comparamos elementos consecutivos y los intercambiamos si el primero es mayor que el segundo.
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Intercambiamos los elementos arr[j] y arr[j+1].
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", arr)
    bubble_sort(arr)
    print("Lista ordenada:", arr)
