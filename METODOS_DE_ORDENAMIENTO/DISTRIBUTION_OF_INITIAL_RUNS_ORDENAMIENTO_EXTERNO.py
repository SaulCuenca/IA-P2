def distribute_initial_runs(arr, k):
    # Dividimos la lista en subsecuencias aproximadamente del mismo tamaño.
    n = len(arr)
    subsequence_size = n // k
    initial_runs = []

    for i in range(k):
        start = i * subsequence_size
        end = start + subsequence_size

        if i == k - 1:
            # Ajuste para la Ultima subsecuencia.
            end = n

        subsequence = arr[start:end]
        initial_runs.append(subsequence)

    return initial_runs

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [7, 2, 8, 4, 1, 9, 3, 6, 5]
    k = 3  # Numero de subsecuencias iniciales
    print("Lista original:", arr)
    initial_runs = distribute_initial_runs(arr, k)
    print("Distribucion de subsecuencias iniciales:")
    for i, run in enumerate(initial_runs):
        print(f"Subsecuencia {i + 1}: {run}")

