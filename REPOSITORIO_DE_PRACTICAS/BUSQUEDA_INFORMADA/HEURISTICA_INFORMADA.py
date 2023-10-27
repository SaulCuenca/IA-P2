import heapq  # Importa la biblioteca heapq para gestionar la frontera (cola de prioridad).

class Nodo:  # Define la clase Nodo que se utilizará para representar nodos en el grafo.
    def __init__(self, estado, padre=None, costo=0, heuristica=0):
        # Inicializa un nodo con un estado, un nodo padre (padre), un costo acumulado (costo) y una heuristica (heuristica).
        self.estado = estado  # El estado representa la ubicación o posición actual en el grafo.
        self.padre = padre    # El padre es el nodo del que se expandió este nodo.
        self.costo = costo    # El costo acumulado es el costo total para llegar a este nodo desde el inicio.
        self.heuristica = heuristica  # La heuristica es una estimación del costo restante para llegar al objetivo.
        self.total = costo + heuristica  # El costo total es la suma del costo acumulado y la heuristica.

    def __lt__(self, other):
        # Define el método de comparación para que los nodos se puedan ordenar según su costo total.
        return self.total < other.total

def a_estrella(grafo, estado_inicial, estado_objetivo, heuristica):
    inicio = Nodo(estado_inicial, None, 0, heuristica(estado_inicial))  # Crea un nodo inicial.
    frontera = [inicio]  # Inicializa la frontera como una lista con el nodo inicial.
    explorados = set()  # Inicializa un conjunto para realizar un seguimiento de los nodos explorados.

    while frontera:  # Mientras la frontera no esté vacía.
        nodo_actual = heapq.heappop(frontera)  # Obtiene el nodo con el costo total mínimo de la frontera.

        if nodo_actual.estado == estado_objetivo:  # Si el nodo actual es el objetivo, se ha encontrado el camino.
            return construir_camino(nodo_actual)  # Llama a una función para construir el camino desde el nodo actual.

        explorados.add(nodo_actual.estado)  # Agrega el estado del nodo actual a los nodos explorados.

        for vecino, costo in grafo[nodo_actual.estado]:  # Itera sobre los vecinos del nodo actual.
            if vecino not in explorados:  # Si el vecino no ha sido explorado.
                nuevo_costo = nodo_actual.costo + costo  # Calcula el nuevo costo acumulado.
                nueva_heuristica = heuristica(vecino)    # Calcula la nueva heurística para el vecino.
                nuevo_nodo = Nodo(vecino, nodo_actual, nuevo_costo, nueva_heuristica)  # Crea un nuevo nodo.

                if any(nodo.total <= nuevo_nodo.total for nodo in frontera):
                    continue  # Si hay un nodo en la frontera con un costo total menor o igual, continúa con el siguiente vecino.

                heapq.heappush(frontera, nuevo_nodo)  # Agrega el nuevo nodo a la frontera.

    return None  # Si no se encuentra un camino, devuelve None.

def construir_camino(nodo):
    camino = []  # Inicializa una lista para almacenar el camino.
    while nodo:  # Mientras haya un nodo valido.
        camino.append(nodo.estado)  # Agrega el estado del nodo al camino.
        nodo = nodo.padre  # Avanza al nodo padre.
    return list(reversed(camino))  # Invierte el camino para que esté en el orden correcto.

# Ejemplo de grafo con conexiones y costos.
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1), ('E', 3)],
    'E': [('D', 3)]
}

# Función heuristica simple (distancia euclidiana).
def heuristica_euclidiana(estado):
    objetivos = {
        'A': (2, 4),
        'B': (1, 3),
        'C': (2, 1),
        'D': (4, 2),
        'E': (5, 5)
    }
    x1, y1 = objetivos[estado]
    x2, y2 = objetivos['E']
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5  # Calcula la distancia euclidiana.

inicio = 'A'  # Define el estado inicial.
objetivo = 'E'  # Define el estado objetivo.

camino = a_estrella(grafo, inicio, objetivo, heuristica_euclidiana)  # Ejecuta la busqueda A*.

if camino:  # Si se encontro un camino.
    print(f'Ruta mas corta de {inicio} a {objetivo}: {camino}')  # Imprime el camino.
    print(f'Costo total: {len(camino) - 1}')  # Imprime el costo total (longitud del camino - 1).
else:
    print(f'No se encontro una ruta de {inicio} a {objetivo}.')  # Imprime un mensaje si no se encontró un camino.

