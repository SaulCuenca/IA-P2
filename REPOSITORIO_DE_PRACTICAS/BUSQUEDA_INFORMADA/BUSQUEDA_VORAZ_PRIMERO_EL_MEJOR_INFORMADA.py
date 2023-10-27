def busqueda_voraz_primero_el_mejor(estado_inicial, es_objetivo, generar_sucesores, funcion_evaluacion):
    frontera = [(estado_inicial, 0)]  # Cola de prioridad con tuplas (estado, valor)
    
    while frontera:
        estado_actual, valor_actual = frontera.pop(0)  # Tomar el estado con el valor mas alto
        if es_objetivo(estado_actual):
            return estado_actual  # Hemos encontrado el estado objetivo
        
        sucesores = generar_sucesores(estado_actual)
        for sucesor in sucesores:
            valor_sucesor = funcion_evaluacion(sucesor)
            frontera.append((sucesor, valor_sucesor))
            frontera.sort(key=lambda x: x[1])  # Ordenar la frontera por valor
    
    return None  # No se encontro una soluci�n

# Ejemplo de uso
def es_objetivo(estado):
    return estado == 8

def generar_sucesores(estado):
    return [estado + 1, estado + 2]

def funcion_evaluacion(estado):
    return abs(estado - 8)

estado_inicial = 0
solucion = busqueda_voraz_primero_el_mejor(estado_inicial, es_objetivo, generar_sucesores, funcion_evaluacion)

if solucion is not None:
    print(f"Solucion encontrada: {solucion}")
else:
       print("No se encontro una solucion.")

# En este ejemplo, el algoritmo de busqueda voraz "Primero el Mejor" se utiliza para encontrar una soluci�n al problema de llegar al estado objetivo 8 desde el estado inicial 0. La funcion de evaluacion funcion_evaluacion mide la distancia entre el estado actual y el estado objetivo. El algoritmo selecciona el sucesor con la menor distancia en cada paso.

#Ten en cuenta que este algoritmo de b�squeda voraz no garantiza la optima soluci�n en todos los casos y puede quedar atrapado en m�nimos locales. 
