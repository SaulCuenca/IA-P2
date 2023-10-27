def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Ejemplo de un grafo representado como un diccionario de adyacencia
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Recorrido en profundidad (DFS):")
dfs(graph, 'A')

#La busqueda en profundidad es un algoritmo de b�squeda que se utiliza com�nmente en la resoluci�n de problemas y en la exploraci�n de estructuras de datos como �rboles y grafos.
