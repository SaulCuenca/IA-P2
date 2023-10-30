# FunciOn para calcular la probabilidad de obtener un número especifico en un dado justo
def probabilidad_dado(numero_deseado):
    numero_posibilidades = 6
    probabilidad_individual = 1 / numero_posibilidades
    return probabilidad_individual

# Calcular la probabilidad de obtener un numero especifico en ambos dados (independientes)
numero_deseado_A = 4  # Número deseado en el dado A
numero_deseado_B = 3  # Número deseado en el dado B

probabilidad_A = probabilidad_dado(numero_deseado_A)
probabilidad_B = probabilidad_dado(numero_deseado_B)

# La probabilidad conjunta es simplemente el producto de las probabilidades individuales
probabilidad_conjunta = probabilidad_A * probabilidad_B

print(f"Probabilidad de obtener un {numero_deseado_A} en el dado A: {probabilidad_A}")
print(f"Probabilidad de obtener un {numero_deseado_B} en el dado B: {probabilidad_B}")
print(f"Probabilidad conjunta de obtener ambos numeros: {probabilidad_conjunta}")
