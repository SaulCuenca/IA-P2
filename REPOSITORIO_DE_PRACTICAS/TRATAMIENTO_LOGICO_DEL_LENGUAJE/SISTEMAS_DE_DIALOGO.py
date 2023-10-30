import random

# Definimos un diccionario de preguntas y respuestas
dialogo = {
    "Hola": "�Hola! �En qu� puedo ayudarte?",
    "�C�mo est�s?": "Estoy bien, gracias por preguntar.",
    "�Cu�l es tu nombre?": "Soy un asistente virtual.",
    "�Qu� tiempo hace hoy?": "Lo siento, no tengo acceso a informaci�n en tiempo real.",
    "Adi�s": "Hasta luego. �Ten un buen d�a!",
}

# Funci�n para procesar preguntas y generar respuestas
def responder_pregunta(pregunta):
    pregunta = pregunta.lower()
    respuesta = dialogo.get(pregunta, "Lo siento, no entiendo la pregunta.")
    return respuesta

# Loop de di�logo
while True:
    pregunta = input("T�: ")
    if pregunta.lower() == "adi�s":
        print("Asistente: Hasta luego. �Ten un buen d�a!")
        break
    respuesta = responder_pregunta(pregunta)
    print("Asistente:", respuesta)
