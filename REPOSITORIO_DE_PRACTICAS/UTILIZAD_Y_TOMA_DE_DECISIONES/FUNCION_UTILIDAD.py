# Funci�n para verificar si un n�mero es par
def es_par(numero):
    return numero % 2 == 0

# Funci�n para verificar si un n�mero es primo
def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

# Funci�n para calcular el factorial de un n�mero
def factorial(numero):
    if numero == 0:
        return 1
    return numero * factorial(numero - 1)

# Funci�n para convertir una lista de cadenas en una sola cadena separada por comas
def lista_a_cadena(lista):
    return ', '.join(lista)

# Funci�n para verificar si una cadena es un pal�ndromo
def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

# Ejemplos de uso
if __name__ == "__main":
    print(es_par(4))  # True
    print(es_primo(17))  # True
    print(factorial(5))  # 120
    print(lista_a_cadena(["manzana", "banana", "naranja"]))  # "manzana, banana, naranja"
    print(es_palindromo("anilina"))  # True
