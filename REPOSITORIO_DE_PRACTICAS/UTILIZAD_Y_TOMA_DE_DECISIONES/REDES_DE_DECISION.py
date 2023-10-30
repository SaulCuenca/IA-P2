import networkx as nx

# Crear un grafico de red de decision
G = nx.DiGraph()

# Agregar nodos (eventos y decisiones)
G.add_node("Iniciar", type="decision")
G.add_node("Llueve", type="event")
G.add_node("Trafico", type="event")
G.add_node("Llegar tarde", type="event")
G.add_node("Tomar sombrilla", type="decision")

# Agregar bordes entre los nodos
G.add_edge("Iniciar", "Llueve")
G.add_edge("Iniciar", "Trafico")
G.add_edge("Llueve", "Tomar sombrilla")
G.add_edge("Trafico", "Llegar tarde")
G.add_edge("Llegar tarde", "Tomar sombrilla")

# Asignar probabilidades a los eventos
G.nodes["Llueve"]["prob"] = 0.3
G.nodes["Trafico"]["prob"] = 0.4
G.nodes["Llegar tarde"]["prob"] = 0.2

# Asignar valores a las decisiones
G.nodes["Iniciar"]["value"] = 0
G.nodes["Tomar sombrilla"]["value"] = 5

# Calcular el valor esperado
def calcular_valor_esperado(G):
    valor_esperado = 0
    for nodo in nx.topological_sort(G):
        if G.nodes[nodo]["type"] == "event":
            padre = list(G.predecessors(nodo))[0]
            valor_esperado += G.nodes[nodo]["prob"] * G.nodes[padre]["value"]
    return valor_esperado

valor_esperado = calcular_valor_esperado(G)
print(f"El valor esperado de la red de decision es: {valor_esperado}")
#hemos creado una red de decisión simple que modela la decision de si llevar una sombrilla en función de si llueve, si hay trafico y si llegas tarde. Luego, calculamos el valor esperado de tomar la decisión de llevar una sombrilla. Puedes personalizar este codigo para adaptarlo a tu problema específico y añadir mas nodos y aristas según sea necesario.
