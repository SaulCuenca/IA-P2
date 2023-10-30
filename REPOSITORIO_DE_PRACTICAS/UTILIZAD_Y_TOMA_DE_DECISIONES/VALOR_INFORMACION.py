import random

# Supongamos que la probabilidad de lluvia sin información es del 30%
probabilidad_sin_informacion = 0.3

# Supongamos que llevar un paraguas cuesta $10 y te ahorraría $50 si llueve
costo_paraguas = 10
ahorro_si_llueve = 50

# Función para calcular el valor de la informacion
def valor_informacion(probabilidad_sin_info, costo_paraguas, ahorro_si_llueve):
    # Valor esperado sin información
    valor_sin_informacion = probabilidad_sin_info * ahorro_si_llueve

    # Simulación de informacion adicional (pronóstico del tiempo)
    # Supongamos que el pronostico puede ser "lluvia" o "no lluvia" con ciertas probabilidades
    pronostico = random.choice(["lluvia", "no lluvia"])

    # Supongamos que el pronostico "lluvia" tiene una probabilidad del 60%
    probabilidad_con_informacion = 0.6 if pronostico == "lluvia" else 0.4

    # Valor esperado con informacion
    valor_con_informacion = probabilidad_con_informacion * ahorro_si_llueve

    # Valor de la información
    valor_info = valor_con_informacion - valor_sin_informacion

    return valor_info

# Calcular el valor de la información
valor_info = valor_informacion(probabilidad_sin_informacion, costo_paraguas, ahorro_si_llueve)

# Imprimir resultados
print(f"Valor de la informacion sobre el pronostico del tiempo: ${valor_info:.2f}")

# Tomar la decision
if valor_info > costo_paraguas:
    print("Deberias consultar el pronostico y llevar un paraguas si es favorable.")
else:
    print("No es necesario consultar el pronostico del tiempo.")
