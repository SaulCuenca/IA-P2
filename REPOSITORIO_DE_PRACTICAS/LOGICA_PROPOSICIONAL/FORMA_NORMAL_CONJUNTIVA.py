from sympy import symbols, Or, And, Not, to_cnf, simplify

# Definimos las variables simb�licas
p, q, r = symbols('p q r')

# Definimos la f�rmula original
formula_original = And(Or(p, q), Or(Not(p), r))

# Convertimos la f�rmula a Forma Normal Conjuntiva (FNC)
formula_fnc = to_cnf(formula_original, True)

# Aplicamos simplificaciones adicionales para obtener una FNC m�s simple
formula_fnc_simplificada = simplify(formula_fnc)

print("F�rmula Original:")
print(formula_original)
print("\nF�rmula en Forma Normal Conjuntiva (FNC):")
print(formula_fnc)
print("\nF�rmula FNC Simplificada:")
print(formula_fnc_simplificada)
