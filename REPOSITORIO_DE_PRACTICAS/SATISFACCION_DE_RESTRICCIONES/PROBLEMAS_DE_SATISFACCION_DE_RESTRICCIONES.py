from constraint import Problem

# Define el problema
problem = Problem()

# Define las variables (pa�ses) y sus dominios (colores)
countries = ["A", "B", "C", "D"]
colors = ["Red", "Green", "Blue"]

for country in countries:
    problem.addVariable(country, colors)

# Define las restricciones (pa�ses adyacentes no pueden tener el mismo color)
problem.addConstraint(lambda a, b: a != b, ("A", "B"))
problem.addConstraint(lambda a, b: a != b, ("A", "C"))
problem.addConstraint(lambda a, b: a != b, ("A", "D"))
problem.addConstraint(lambda b, c: b != c, ("B", "C"))
problem.addConstraint(lambda c, d: c != d, ("C", "D"))

# Encuentra la solucion
solutions = problem.getSolutions()

# Imprime las soluciones encontradas
for solution in solutions:
    print(solution)
