
import numpy as np

# Definir el MDP
# - S: Conjunto de estados
# - A: Conjunto de acciones
# - P: Funcion de transici�n de probabilidad
# - R: Funcion de recompensa
# - gamma: Factor de descuento

# Ejemplo MDP: Dos estados (S={0, 1}), dos acciones (A={0, 1}), recompensas constantes, factor de descuento 0.9
S = [0, 1]
A = [0, 1]
P = {
    0: {
        0: {0: 0.7, 1: 0.3},
        1: {0: 0.3, 1: 0.7}
    },
    1: {
        0: {0: 0.1, 1: 0.9},
        1: {0: 0.4, 1: 0.6}
    }
}
R = {0: {0: 5, 1: -2}, 1: {0: 1, 1: -1}}
gamma = 0.9

# Inicializacion de los valores de los estados
V = {s: 0 for s in S}

# Iteracion de Valor
num_iterations = 100
for _ in range(num_iterations):
    V_new = {}
    for s in S:
        max_q_value = float('-inf')
        for a in A:
            q_value = sum(P[s][a][s_prime] * (R[s][a] + gamma * V[s_prime]) for s_prime in S)
            max_q_value = max(max_q_value, q_value)
        V_new[s] = max_q_value
    V = V_new

# Pol�tica optima
policy = {}
for s in S:
    max_q_action = None
    max_q_value = float('-inf')
    for a in A:
        q_value = sum(P[s][a][s_prime] * (R[s][a] + gamma * V[s_prime]) for s_prime in S)
        if q_value > max_q_value:
            max_q_value = q_value
            max_q_action = a
    policy[s] = max_q_action

# Imprimir la politica optima
print("Politica optima:")
for s, a in policy.items():
    print(f"Estado {s}: Accion {a}")
#Un proceso de decision de Markov (MDP) es un modelo matematico que se utiliza en el aprendizaje automatico y la toma de decisiones secuenciales. 
#Este codigo implementa un proceso de decision de Markov simple con dos estados y dos acciones. A traves de la iteraci�n de valor, encuentra la pol�tica optima y la muestra en la salida. Ten en cuenta que este es un ejemplo muy basico, y los MDPs en la practica pueden ser mucho mas complejos.