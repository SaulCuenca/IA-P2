def iddfs(graph, start, goal):
    depth = 0
    while True:
        visited = set()
        result = dls(graph, start, goal, depth, visited)
        if result == goal:
            return result
        depth += 1

def dls(graph, node, goal, depth, visited):
    if depth == 0 and node == goal:
        return node
    elif depth > 0:
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                result = dls(graph, neighbor, goal, depth - 1, visited)
                if result == goal:
                    return result
    return None

# Ejemplo de un grafo representado como un diccionario de adyacencia
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
goal_node = 'F'

print("Busqueda en Profundidad Iterativa (IDDFS):")
result = iddfs(graph, start_node, goal_node)

if result is not None:
    print(f"Se encontro un camino de {start_node} a {goal_node}: {result}")
else:
    print(f"No se encontro un camino de {start_node} a {goal_node}.")

    #La busqueda en profundidad iterativa (Iterative Deepening Depth-First Search, IDDFS) es una estrategia de b�squeda que combina la profundidad de la b�squeda en profundidad (DFS) con la iteraci�n progresiva para encontrar soluciones en un grafo con una profundidad desconocida.
    #En este c�digo, la funci�n iddfs realiza la b�squeda en profundidad iterativa. Comienza con una profundidad de b�squeda de 0 y aumenta progresivamente la profundidad hasta encontrar la soluci�n o determinar que no existe. La funci�n dls realiza la b�squeda en profundidad limitada (DLS) para cada iteraci�n, con la profundidad especificada.
