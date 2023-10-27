def normalize_signal(signal):
    # Calcula el valor maximo y minimo en la se�al
    max_value = max(signal)
    min_value = min(signal)
    
    # Normaliza la senal en un rango de 0 a 1
    normalized_signal = [(x - min_value) / (max_value - min_value) for x in signal]
    
    return normalized_signal

# Ejemplo de uso
input_signal = [10, 20, 30, 40, 50]
normalized_signal = normalize_signal(input_signal)
print(normalized_signal)
#Este c�digo calcula el valor maximo y m�nimo en la se�al de entrada y luego normaliza los valores para que est�n en un rango de 0 a 1. Puedes adaptar este c�digo a tus necesidades espec�ficas de acondicionamiento de se�ales.

#Si tienes un tipo de senal o acondicionamiento en mente, por favor proporciona m�s detalles para que pueda ayudarte a crear un c�digo m�s espec�fico.
