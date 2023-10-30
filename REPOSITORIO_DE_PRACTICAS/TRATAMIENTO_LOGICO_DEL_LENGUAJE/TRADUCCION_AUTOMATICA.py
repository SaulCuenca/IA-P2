from translate import Translator

# Texto a traducir
texto = "Hello, how are you?"

# Crear un objeto Translator
traductor = Translator(to_lang="es")

# Realizar la traducción
texto_traducido = traductor.translate(texto)

# Imprimir el resultado
print("Texto original: ", texto)
print("Texto traducido: ", texto_traducido)
