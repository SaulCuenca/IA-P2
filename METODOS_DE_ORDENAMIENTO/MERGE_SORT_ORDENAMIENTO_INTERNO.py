def merge_sort(arr):
    # Comprobamos si la longitud de la lista es 0 o 1.
    if len(arr) <= 1:
        return arr

    # Dividimos la lista en mitades.
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Llamamos recursivamente a merge_sort en ambas mitades.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Fusionamos las mitades ordenadas.
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0

    # Combinamos las dos mitades ordenadas en una lista ordenada.
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    # Agregamos los elementos restantes de ambas mitades (si los hay).
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])

    return merged

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Lista original:", arr)
    sorted_arr = merge_sort(arr)
    print("Lista ordenada:", sorted_arr)

