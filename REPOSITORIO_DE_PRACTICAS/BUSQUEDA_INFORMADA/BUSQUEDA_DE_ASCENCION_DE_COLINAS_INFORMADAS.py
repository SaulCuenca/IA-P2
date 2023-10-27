import random

# Funcion de ejemplo para la optimización. Reemplazala con tu propia función.
def objective_function(x):
    return -x**2 + 4*x - 4

def hill_climbing(max_iterations):
    # Generar un punto inicial aleatorio
    current_solution = random.uniform(-10, 10)
    current_value = objective_function(current_solution)

    for _ in range(max_iterations):
        # Generar un vecino cercano
        neighbor = current_solution + random.uniform(-0.1, 0.1)
        neighbor_value = objective_function(neighbor)

        # Si el vecino es mejor, muevete a el
        if neighbor_value > current_value:
            current_solution = neighbor
            current_value = neighbor_value

    return current_solution, current_value

if __name__ == "__main__":
    max_iterations = 1000
    best_solution, best_value = hill_climbing(max_iterations)

    print("Mejor solucion encontrada:", best_solution)
    print("Valor de la funcion en la mejor solucion:", best_value)

    #La busqueda de ascenso de colinas, o Hill Climbing en ingles, es un algoritmo de optimización que se utiliza para encontrar un maximo local en una funcion. 
    #El algoritmo comienza con una solucion aleatoria y realiza iteraciones para buscar vecinos cercanos que tengan un valor de función superior. Si encuentra un vecino mejor, se mueve hacia él.
