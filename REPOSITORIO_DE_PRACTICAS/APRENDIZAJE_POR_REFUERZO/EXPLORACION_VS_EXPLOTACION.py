import numpy as np

# Numero de brazos en el bandit multi-armed
num_brazos = 5

# Verdadera recompensa media para cada brazo (puede ser desconocida en la practica)
recompensas_verdaderas = np.random.normal(0, 1, num_brazos)

# Inicializacion del promedio estimado de recompensas y recuento de selecci�n de brazos
promedio_estimado = np.zeros(num_brazos)
contador_seleccion = np.zeros(num_brazos)

# Numero total de iteraciones (tiradas de brazo)
num_iteraciones = 1000

# Parametro epsilon para equilibrar exploraci�n y explotaci�n
epsilon = 0.1

# Historial de recompensas obtenidas
recompensas_historial = []

for i in range(num_iteraciones):
    if np.random.random() < epsilon:
        # Exploracion: elige un brazo al azar
        brazo_elegido = np.random.choice(num_brazos)
    else:
        # Explotacion: elige el brazo con el promedio estimado mas alto
        brazo_elegido = np.argmax(promedio_estimado)

    # Simular la recompensa para el brazo elegido
    recompensa = np.random.normal(recompensas_verdaderas[brazo_elegido], 1)
    
    # Actualizar el promedio estimado y el contador de selecci�n del brazo
    contador_seleccion[brazo_elegido] += 1
    promedio_estimado[brazo_elegido] += (recompensa - promedio_estimado[brazo_elegido]) / contador_seleccion[brazo_elegido]

    # Registrar la recompensa obtenida en el historial
    recompensas_historial.append(recompensa)

# Calcular la recompensa total acumulada
recompensa_total = sum(recompensas_historial)

print(f"Recompensa total acumulada: {recompensa_total}")

# Puedes analizar el historial de recompensas obtenidas para evaluar el rendimiento
#Este codigo implementa un algoritmo epsilon-greedy para equilibrar la exploraci�n (con probabilidad epsilon) y la explotacion (con probabilidad 1 - epsilon) en un problema de bandit multi-armed. Puedes ajustar el valor de epsilon para controlar el equilibrio entre exploracion y explotacion. Cuanto menor sea epsilon, mas enfasis se pondra en la explotacion.

#Ten en cuenta que en un entorno real, las recompensas verdaderas no serian conocidas, pero este ejemplo las simula para ilustrar el concepto. En la practica, tendrias que adaptar el algoritmo para aprender de las recompensas observadas.






Re
