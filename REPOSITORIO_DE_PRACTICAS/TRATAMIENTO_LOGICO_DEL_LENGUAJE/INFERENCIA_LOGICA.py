from sympy import symbols, Implies, And, Not, simplify_logic

# Definimos las variables simbólicas
p, q, r = symbols('p q r')

# Definimos una premisa lógica
premisa = Implies(p, And(q, r))

# Definimos una afirmación adicional
afirmacion = Not(q)

# Realizamos una inferencia lógica
conclusion = simplify_logic(Implies(premisa, afirmacion))

# Imprimimos la conclusión
print(conclusion)
