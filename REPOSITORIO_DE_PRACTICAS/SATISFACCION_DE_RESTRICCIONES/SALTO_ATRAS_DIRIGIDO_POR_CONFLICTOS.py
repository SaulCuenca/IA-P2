class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.assignment = {}

    def is_complete(self):
        return len(self.assignment) == len(self.variables)

    def is_consistent(self, var, value):
        for constraint in self.constraints[var]:
            if not constraint(self.assignment):
                return False
        return True

    def backjumping_search(self):
        if self.is_complete():
            return self.assignment

        var = self.select_unassigned_variable()
        for value in self.order_domain_values(var):
            if self.is_consistent(var, value):
                self.assignment[var] = value
                result = self.backjumping_search()
                if result is not None:
                    return result
                del self.assignment[var]
        return None

    def select_unassigned_variable(self):
        for var in self.variables:
            if var not in self.assignment:
                return var

    def order_domain_values(self, var):
        return self.domains[var]

def main():
    variables = ["A", "B", "C"]
    domains = {
        "A": [1, 2, 3],
        "B": [1, 2, 3],
        "C": [1, 2, 3]
    }
    constraints = {
        "A": [lambda assignment: assignment["A"] != assignment["B"]],
        "B": [lambda assignment: assignment["A"] != assignment["B"],
              lambda assignment: assignment["B"] != assignment["C"]],
        "C": [lambda assignment: assignment["B"] != assignment["C"]]
    }

    csp = CSP(variables, domains, constraints)
    solution = csp.backjumping_search()
    if solution is not None:
        print("Solution found:")
        for var, value in solution.items():
            print(f"{var}: {value}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
#El algoritmo de Salto Atras Dirigido por Conflictos (Backjumping) es una tecnica utilizada en la resolucion de problemas de satisfaccion de restricciones (CSPs) que permite identificar de manera eficiente cual variable o asignaci�n es responsable de un conflicto en la busqueda.
#Este codigo define una clase CSP para representar un problema de satisfaccion de restricciones. Puedes personalizar las variables, dominios y restricciones para adaptarlas a tu problema especifico. El metodo backjumping_search implementa el algoritmo de Salto Atr�s Dirigido por Conflictos. Ten en cuenta que este codigo es solo un ejemplo simple y puede requerir modificaciones para adaptarse a casos mas complejos.
