from sympy import symbols, Implies, Equivalent, And, Or, Not, satisfiable, ask

# Definimos las variables simb�licas
p, q, r = symbols('p q r')

# Definimos dos expresiones l�gicas
expresion1 = Equivalent(Implies(p, q), Or(Not(p), q))  # Ley de implicaci�n
expresion2 = And(Or(p, q), Or(Not(p), r))  # Expresi�n conjuntiva

# Verificamos la equivalencia de las expresiones
if expresion1.equals(expresion2):
    print("Las expresiones son equivalentes.")
else:
    print("Las expresiones no son equivalentes.")

# Verificamos la validez de una expresi�n (si es verdadera para todas las asignaciones)
expresion3 = Or(p, Not(p))
if ask(expresion3, True):
    print("La expresi�n es v�lida (siempre verdadera).")
else:
    print("La expresi�n no es v�lida.")

# Verificamos la satisfacibilidad de una expresi�n (si es verdadera para al menos una asignaci�n)
expresion4 = And(p, Not(q))
if satisfiable(expresion4):
    print("La expresi�n es satisfacible (al menos una asignaci�n la hace verdadera).")
else:
    print("La expresi�n no es satisfacible (siempre falsa).")
