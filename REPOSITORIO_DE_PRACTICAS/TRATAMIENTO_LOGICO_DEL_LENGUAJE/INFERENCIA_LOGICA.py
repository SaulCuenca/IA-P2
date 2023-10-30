from sympy import symbols, Implies, And, Not, simplify_logic

# Definimos las variables simb�licas
p, q, r = symbols('p q r')

# Definimos una premisa l�gica
premisa = Implies(p, And(q, r))

# Definimos una afirmaci�n adicional
afirmacion = Not(q)

# Realizamos una inferencia l�gica
conclusion = simplify_logic(Implies(premisa, afirmacion))

# Imprimimos la conclusi�n
print(conclusion)
