import sys

def prim_mst(graph):
    num_vertices = len(graph)
    # Inicializamos un conjunto vacio para almacenar los nodos visitados.
    visited = [False] * num_vertices
    # Inicializamos una lista para almacenar los bordes del MST.
    mst = [None] * num_vertices
    # Inicializamos la distancia de cada nodo a infinito.
    key = [sys.maxsize] * num_vertices
    # Elegimos un nodo de inicio (puedes personalizarlo según tu gráfico).
    start_node = 0
    key[start_node] = 0

    for _ in range(num_vertices):
        # Encuentra el nodo con la distancia minima no visitado.
        min_key = sys.maxsize
        min_index = -1
        for v in range(num_vertices):
            if not visited[v] and key[v] < min_key:
                min_key = key[v]
                min_index = v

        visited[min_index] = True

        # Agregamos el borde a la lista del MST.
        if mst[min_index] is not None:
            print(f"Arista: {mst[min_index]} - Peso: {key[min_index]}")

        for v in range(num_vertices):
            if (
                graph[min_index][v] != 0
                and not visited[v]
                and graph[min_index][v] < key[v]
            ):
                key[v] = graph[min_index][v]
                mst[v] = f"{min_index}-{v}"

# Ejemplo de grafo ponderado en forma de matriz de adyacencia.
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0],
]

print("Pasos para construir el arbol Parcial Minimo de Prim:")
prim_mst(graph)
