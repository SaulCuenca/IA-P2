def polyphase_sort(arr, k):
    n = len(arr)
    p = n // k
    runs = []

    # Dividimos la lista en k subsecuencias.
    for i in range(k):
        runs.append(arr[i * p:(i + 1) * p])

    # Creamos k bloques iniciales.
    blocks = [[] for _ in range(k)]

    # Realizamos la fase inicial de ordenamiento interno para cada bloque.
    for i in range(k):
        runs[i].sort()
        blocks[i].append(runs[i].pop(0))

    sorted_arr = []

    while any(runs):
        for i in range(k):
            if len(blocks[i]) == p:
                continue
            if not runs[i]:
                for j in range(i + 1, k):
                    if runs[j]:
                        runs[i].append(blocks[j].pop(0))
                        break
                else:
                    runs[i].append(blocks[i].pop(0))

            min_value = min(runs[i])
            sorted_arr.append(min_value)
            runs[i].remove(min_value)
            blocks[i].append(min_value)

    return sorted_arr

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [4, 9, 3, 6, 7, 1, 8, 5, 2]
    k = 3  # Número de bloques
    print("Lista original:", arr)
    sorted_arr = polyphase_sort(arr, k)
    print("Lista ordenada:", sorted_arr)

