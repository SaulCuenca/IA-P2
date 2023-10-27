def natural_merge_sort(arr):
    # Inicializamos una lista vacía para almacenar las secuencias ordenadas.
    sorted_sequences = []

    # Separamos la lista en secuencias ordenadas.
    current_sequence = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            current_sequence.append(arr[i])
        else:
            sorted_sequences.append(current_sequence)
            current_sequence = [arr[i]]

    sorted_sequences.append(current_sequence)

    # Combinamos las secuencias ordenadas hasta que quede una sola lista ordenada.
    while len(sorted_sequences) > 1:
        sorted_sequences = merge(sorted_sequences)

    return sorted_sequences[0]

def merge(sequences):
    result = []
    while sequences:
        smallest = min(sequences, key=lambda seq: seq[0])
        result.append(smallest.pop(0))
        if not smallest:
            sequences.remove(smallest)
    return result

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [12, 4, 5, 6, 7, 3, 1, 15]
    print("Lista original:", arr)
    sorted_arr = natural_merge_sort(arr)
    print("Lista ordenada:", sorted_arr)

