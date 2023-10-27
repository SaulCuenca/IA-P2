def ldfs(graph, start, limit, depth=0):
    if depth > limit:
        return
    
    print(start, end=' ')

    for neighbor in graph[start]:
        ldfs(graph, neighbor, limit, depth + 1)

# Ejemplo de un grafo representado como un diccionario de adyacencia
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Busqueda en Profundidad Limitada (LDFS):")
ldfs(graph, 'A', 2)  # Limitar la profundidad a 2

#La busqueda en profundidad limitada (Limited Depth-First Search, LDFS) es una variante de la b�squeda en profundidad (DFS) en la que se establece un l�mite m�ximo en la profundidad hasta la cual se explorar�n los nodos. 
#Si la profundidad actual supera el l�mite establecido, la funci�n retorna sin explorar m�s all� de ese punto. De lo contrario, sigue explorando los nodos vecinos hasta el l�mite de profundidad establecido.
