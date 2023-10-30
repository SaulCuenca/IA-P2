from sympy import symbols, Not, And, Or, Implies, Equivalent

# Definimos las variables simb�licas
p, q = symbols('p q')

# Creamos expresiones l�gicas
expresion1 = And(p, q)  # p AND q
expresion2 = Or(p, q)   # p OR q
expresion3 = Implies(p, q)  # p IMPLIES q
expresion4 = Equivalent(p, q)  # p IF AND ONLY IF q

# Imprimimos las expresiones l�gicas
print("Expresi�n 1 (p AND q):", expresion1)
print("Expresi�n 2 (p OR q):", expresion2)
print("Expresi�n 3 (p IMPLIES q):", expresion3)
print("Expresi�n 4 (p IF AND ONLY IF q):", expresion4)

# Evaluamos las expresiones para algunos valores de p y q
valores = [(True, True), (True, False), (False, True), (False, False)]

for p_valor, q_valor in valores:
    resultado1 = expresion1.subs({p: p_valor, q: q_valor})
    resultado2 = expresion2.subs({p: p_valor, q: q_valor})
    resultado3 = expresion3.subs({p: p_valor, q: q_valor})
    resultado4 = expresion4.subs({p: p_valor, q: q_valor})

    print(f"Para p={p_valor}, q={q_valor}:")
    print(f"Expresi�n 1 (p AND q) = {resultado1}")
    print(f"Expresi�n 2 (p OR q) = {resultado2}")
    print(f"Expresi�n 3 (p IMPLIES q) = {resultado3}")
    print(f"Expresi�n 4 (p IF AND ONLY IF q) = {resultado4}")
    print()

# Tambi�n podemos aplicar negaci�n a una expresi�n l�gica
negacion_expresion1 = Not(expresion1)
print("Negaci�n de la Expresi�n 1 (NOT p AND q):", negacion_expresion1)
