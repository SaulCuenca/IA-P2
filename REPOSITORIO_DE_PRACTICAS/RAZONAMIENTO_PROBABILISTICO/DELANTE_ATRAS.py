import numpy as np

# Definici�n de un modelo oculto de Markov (HMM) simple
# Este HMM tiene dos estados ocultos (A y B) y dos s�mbolos observados (0 y 1)
num_states = 2
num_symbols = 2

# Par�metros iniciales del HMM (transiciones y emisiones)
initial_state_prob = np.array([0.5, 0.5])  # Probabilidades iniciales de los estados
transition_matrix = np.array([[0.7, 0.3], [0.4, 0.6]])  # Matriz de transiciones
emission_matrix = np.array([[0.9, 0.1], [0.2, 0.8]])  # Matriz de emisiones

# Observaciones (secuencia de s�mbolos observados)
observations = [0, 1, 0, 0, 1]

# Algoritmo hacia adelante
def forward_algorithm(observations, initial_state_prob, transition_matrix, emission_matrix):
    num_states = len(initial_state_prob)
    num_observations = len(observations)
    forward_matrix = np.zeros((num_states, num_observations))

    # Inicializaci�n
    forward_matrix[:, 0] = initial_state_prob * emission_matrix[:, observations[0]]

    # Propagaci�n hacia adelante
    for t in range(1, num_observations):
        for s in range(num_states):
            forward_matrix[s, t] = np.sum(forward_matrix[:, t - 1] * transition_matrix[:, s]) * emission_matrix[s, observations[t]]

    # Probabilidad total de la secuencia observada
    likelihood = np.sum(forward_matrix[:, -1])

    return forward_matrix, likelihood

# Algoritmo hacia atras
def backward_algorithm(observations, transition_matrix, emission_matrix):
    num_states = transition_matrix.shape[0]
    num_observations = len(observations)
    backward_matrix = np.zeros((num_states, num_observations))

    # Inicializacion
    backward_matrix[:, -1] = 1.0

    # Propagacion hacia atras
    for t in range(num_observations - 2, -1, -1):
        for s in range(num_states):
            backward_matrix[s, t] = np.sum(transition_matrix[s, :] * emission_matrix[:, observations[t + 1]] * backward_matrix[:, t + 1])

    return backward_matrix

# Calcular las probabilidades posteriores de estados
def state_posteriors(forward_matrix, backward_matrix, likelihood):
    posterior_matrix = forward_matrix * backward_matrix
    posterior_matrix /= likelihood

    return posterior_matrix

# Ejecutar el algoritmo hacia adelante
forward_matrix, likelihood = forward_algorithm(observations, initial_state_prob, transition_matrix, emission_matrix)

# Ejecutar el algoritmo hacia atr�s
backward_matrix = backward_algorithm(observations, transition_matrix, emission_matrix)

# Calcular las probabilidades posteriores de estados
posterior_matrix = state_posteriors(forward_matrix, backward_matrix, likelihood)

print("Probabilidades posteriores de estados:")
print(posterior_matrix)
