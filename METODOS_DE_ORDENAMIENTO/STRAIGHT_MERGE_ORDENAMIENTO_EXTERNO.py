def straight_merge(left, right):
    result = []
    i = j = 0

    # Combinamos las dos secuencias ordenadas en una sola secuencia ordenada.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Agregamos los elementos restantes de ambas secuencias (si los hay).
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Ejemplo de uso:
if __name__ == "__main__":
    left_sequence = [1, 3, 5, 7, 9]
    right_sequence = [2, 4, 6, 8, 10]
    print("Secuencia izquierda:", left_sequence)
    print("Secuencia derecha:", right_sequence)
    merged_sequence = straight_merge(left_sequence, right_sequence)
    print("Secuencia fusionada:", merged_sequence)

