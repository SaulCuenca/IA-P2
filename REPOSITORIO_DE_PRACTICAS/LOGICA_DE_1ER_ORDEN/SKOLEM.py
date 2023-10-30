from sympy import symbols, Not, Or, simplify

# Definici�n de variables
x, y = symbols('x y')

# Expresi�n con cuantificador existencial
existencial_expr = Or(x > 0, Or(Not(y < 0), Not(y > 5)))

# Skolemizaci�n (aproximaci�n)
skolem_expr = simplify(existencial_expr)

print("Expresi�n original con cuantificador existencial:")
print(existencial_expr)
print("Expresi�n skolemizada (aproximada):")
print(skolem_expr)
