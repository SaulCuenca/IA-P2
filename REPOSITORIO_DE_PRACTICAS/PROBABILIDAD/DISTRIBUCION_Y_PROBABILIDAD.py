import numpy as np
import matplotlib.pyplot as plt

# Parametros de la distribucion normal
media = 5  # Media de la distribución
desviacion_estandar = 2  # Desviación estandar de la distribucion

# Generar datos aleatorios siguiendo una distribución normal
num_muestras = 1000
datos = np.random.normal(media, desviacion_estandar, num_muestras)

# Calcular estadísticas básicas
media_datos = np.mean(datos)
desviacion_estandar_datos = np.std(datos)
varianza_datos = np.var(datos)

# Visualizacion del histograma de los datos generados
plt.hist(datos, bins=30, density=True, alpha=0.6, color='g')
plt.xlabel('Valor')
plt.ylabel('Densidad de Probabilidad')
plt.title('Distribucion Normal')
plt.grid(True)

# Mostrar estadisticas
print(f"Media de los datos: {media_datos}")
print(f"Desviacion estandar de los datos: {desviacion_estandar_datos}")
print(f"Varianza de los datos: {varianza_datos}")

# Mostrar el grafico
plt.show()
