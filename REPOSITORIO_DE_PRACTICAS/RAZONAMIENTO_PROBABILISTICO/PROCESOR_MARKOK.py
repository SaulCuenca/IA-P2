import numpy as np

# Definir la matriz de transici�n de estado
# En este ejemplo, tenemos 3 estados: A, B, C
# La matriz de transicion representa las probabilidades de cambiar de un estado a otro.
transition_matrix = np.array([[0.7, 0.2, 0.1],
                              [0.3, 0.4, 0.3],
                              [0.1, 0.6, 0.3]])

# Definir el estado inicial
# En este ejemplo, comenzamos en el estado A
initial_state = 0

# Simulacion de la cadena de Markov
num_steps = 10
current_state = initial_state

print("Secuencia de estados de la cadena de Markov:")
for _ in range(num_steps):
    print(current_state, end=" ")
    # Escoge el proximo estado con base en la matriz de transicion
    current_state = np.random.choice([0, 1, 2], p=transition_matrix[current_state])
