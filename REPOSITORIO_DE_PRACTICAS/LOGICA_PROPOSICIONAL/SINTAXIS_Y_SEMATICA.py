import pandas as pd
from sympy.logic.boolalg import Or, And, Not, Implies, Equivalent
from itertools import product

# Funci�n para generar una tabla de verdad
def tabla_de_verdad(expresion):
    # Obtenemos las variables en la expresi�n
    variables = list(expresion.free_symbols)
    
    # Generamos todas las combinaciones de valores para las variables
    combinaciones = list(product([True, False], repeat=len(variables)))
    
    # Evaluar la expresi�n para cada combinaci�n de valores
    resultados = []
    for combo in combinaciones:
        valores = dict(zip(variables, combo))
        resultado = expresion.subs(valores)
        resultados.append(list(valores.values()) + [resultado])
    
    # Crear un DataFrame de Pandas para la tabla de verdad
    column_names = [str(var) for var in variables] + ["Resultado"]
    tabla = pd.DataFrame(resultados, columns=column_names)
    
    return tabla

# Funci�n para analizar una expresi�n l�gica
def analizar_expresion(expresion_str):
    expresion = eval(expresion_str)  # Eval�a la expresi�n l�gica
    return expresion

def main():
    print("Generador de Tablas de Verdad para L�gica Proposicional")
    expresion_str = input("Ingrese una expresi�n l�gica (usando variables como p, q y operadores como ~, &, |, =>, <=>): ")
    
    try:
        expresion = analizar_expresion(expresion_str)
        tabla = tabla_de_verdad(expresion)
        print("\nTabla de Verdad:")
        print(tabla)
    except Exception as e:
        print("Error al analizar la expresi�n:", e)

if __name__ == "__main__":
    main()
