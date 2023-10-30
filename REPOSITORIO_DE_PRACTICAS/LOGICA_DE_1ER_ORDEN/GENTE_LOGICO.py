class AgenteLogico:
    def __init__(self, nombre):
        self.nombre = nombre

    def tomar_decision(self, informacion):
        if "informacion_importante" in informacion:
            decision = "Tomar acci�n A"
        else:
            decision = "Tomar acci�n B"
        return decision

# Crear un agente l�gico
agente = AgenteLogico("Agente1")

# Simular una situaci�n con informaci�n
informacion = {"informacion_importante": True}

# El agente toma una decisi�n en funci�n de la informaci�n
decision = agente.tomar_decision(informacion)

print(f"{agente.nombre} decide: {decision}")
