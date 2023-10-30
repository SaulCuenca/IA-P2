def calcular_voi(valor_actual, costo_informacion, valor_con_informacion, probabilidad_exito):
    beneficio_con_informacion = probabilidad_exito * valor_con_informacion
    beneficio_sin_informacion = probabilidad_exito * valor_actual
    beneficio_adicional = beneficio_con_informacion - beneficio_sin_informacion
    voi = beneficio_adicional - costo_informacion
    return voi

# Valores de ejemplo
valor_actual = 10000  # Valor actual de la decisi�n
costo_informacion = 2000  # Costo de obtener informaci�n adicional
valor_con_informacion = 12000  # Valor esperado con informacion adicional
probabilidad_exito = 0.7  # Probabilidad de �xito con informaci�n adicional

# Calcular el Valor de la Informaci�n
voi = calcular_voi(valor_actual, costo_informacion, valor_con_informacion, probabilidad_exito)

# Imprimir el resultado
print(f"El Valor de la Informacion es: {voi}")
#El Valor de la Informaci�n (VOI, por sus siglas en ingl�s) es un concepto utilizado en la toma de decisiones para determinar si la obtencion de informaci�n adicional justifica el costo asociado. Calcular el VOI implica comparar el beneficio esperado de obtener informacion adicional con el costo de adquirirla. 
#En este codigo, la funcion calcular_voi toma el valor actual de la decisi�n, el costo de obtener informaci�n adicional, el valor esperado con informaci�n adicional y la probabilidad de exito con informaci�n adicional. Luego, calcula el beneficio adicional que se obtendr�a con la informacion, resta el costo de obtener la informacion y devuelve el Valor de la Informacion. El valor de ejemplo para el VOI se imprime al final del codigo
#Puedes personalizar los valores de ejemplo y utilizar este c�digo como punto de partida para calcular el Valor de la Informaci�n en tus propias decisiones.

