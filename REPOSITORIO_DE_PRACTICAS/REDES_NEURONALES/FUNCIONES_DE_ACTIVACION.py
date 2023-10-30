import numpy as np

#Las funciones de activaci�n son componentes clave en las redes neuronales y modelos de aprendizaje profundo. 
# Estas funciones introducen no linealidad en las salidas de las neuronas, lo que permite que las redes neuronales 
# aprendan a representar relaciones y patrones complejos en los datos. 


#Funci�n de activaci�n Sigmoide:
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Ejemplo de uso
x = 2.0
result = sigmoid(x)
print(f"Sigmoide de {x} es {result}")

#Funci�n de activaci�n Tangente hiperb�lica (Tanh):
def tanh(x):
    return np.tanh(x)

# Ejemplo de uso
x = 2.0
result = tanh(x)
print(f"Tanh de {x} es {result}")

#Funci�n de activaci�n Rectificadora Lineal Unitaria (ReLU):
def relu(x):
    return max(0, x)

# Ejemplo de uso
x = -1.0
result = relu(x)
print(f"ReLU de {x} es {result}")

#Funci�n de activaci�n Softmax:
def softmax(x):
    exp_x = np.exp(x - np.max(x))  # Restamos el m�ximo para evitar problemas num�ricos
    return exp_x / exp_x.sum(axis=0, keepdims=True)

# Ejemplo de uso
x = np.array([2.0, 1.0, 0.1])
result = softmax(x)
print("Softmax de", x, "es", result)
