reglas_diagnosticas = {
    "Regla 1": {"S�ntoma A": "Causa X"},
    "Regla 2": {"S�ntoma B": "Causa Y"},
    "Regla 3": {"S�ntoma A": "Causa Z", "S�ntoma B": "Causa Y"},
    "Regla 4": {"S�ntoma C": "Causa X"}
}

# Funci�n para realizar el diagn�stico
def diagnosticar_sintomas(sintomas, reglas):
    causas_posibles = set()

    for regla, causas in reglas.items():
        sintomas_coincidentes = set(sintomas) & set(causas.keys())
        if sintomas_coincidentes == set(causas.keys()):
            causas_posibles.update(set(causas.values()))

    return causas_posibles

# S�ntomas observados
sintomas_observados = ["S�ntoma A", "S�ntoma C"]

# Realizar el diagn�stico
causas_posibles = diagnosticar_sintomas(sintomas_observados, reglas_diagnosticas)

if causas_posibles:
    print("Posibles causas identificadas:", causas_posibles)
else:
    print("No se pudo identificar una causa con los s�ntomas observados.")
