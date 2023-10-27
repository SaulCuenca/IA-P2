def bidirectional_search(graph, start, goal):
    forward_queue = [start]
    backward_queue = [goal]
    forward_visited = {start}
    backward_visited = {goal}

    while forward_queue and backward_queue:
        # Expand from the forward direction
        current_node = forward_queue.pop(0)
        for neighbor in graph[current_node]:
            if neighbor not in forward_visited:
                forward_visited.add(neighbor)
                forward_queue.append(neighbor)
            if neighbor in backward_visited:
                return neighbor  # Se encontro un nodo de conexi�n

        # Expand from the backward direction
        current_node = backward_queue.pop(0)
        for neighbor in graph[current_node]:
            if neighbor not in backward_visited:
                backward_visited.add(neighbor)
                backward_queue.append(neighbor)
            if neighbor in forward_visited:
                return neighbor  # Se encontro un nodo de conexi�n

    return None  # No se encontro un camino entre los nodos

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

print("Busqueda Bidireccional:")
result = bidirectional_search(graph, start_node, goal_node)

if result is not None:
    print(f"Se encontro un camino de {start_node} a {goal_node}: {result}")
else:
    print(f"No se encontro un camino de {start_node} a {goal_node}.")

#La busqueda bidireccional es una estrategia de b�squeda que busca una soluci�n desde dos direcciones: una desde el nodo inicial y otra desde el nodo objetivo. Esto puede ser m�s eficiente en ciertos casos que una b�squeda unidireccional, ya que reduce la cantidad de nodos que se deben explorar.
# Este c�digo implementa una b�squeda bidireccional en un grafo representado como un diccionario de adyacencia. Comienza desde el nodo inicial y el nodo objetivo y busca conexiones entre ellos. Si encuentra un nodo que est� en ambos lados, se ha encontrado un camino de conexi�n.
     
