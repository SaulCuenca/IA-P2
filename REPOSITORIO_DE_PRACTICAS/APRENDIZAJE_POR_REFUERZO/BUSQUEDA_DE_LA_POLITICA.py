import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Descarga recursos necesarios
nltk.download('punkt')
nltk.download('stopwords')

def search_policy(text, policy_keywords):
    # Tokeniza el texto en palabras
    words = word_tokenize(text)

    # Obtiene palabras de detencion (stop words)
    stop_words = set(stopwords.words('english'))

    # Filtra las palabras de detencion
    words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]

    # Busca las palabras clave de la politica en el texto
    found_keywords = [keyword for keyword in policy_keywords if keyword in words]

    return found_keywords

# Ejemplo de texto en el que buscar la politica
sample_text = "Este es un ejemplo de un texto en el que buscamos una politica. La politica se refiere a las normas y reglas que rigen nuestra organizacion."

# Palabras clave de política que deseas buscar
policy_keywords = ["politica", "normas", "reglas", "organizacion"]

# Realiza la busqueda de politica en el texto
found_keywords = search_policy(sample_text, policy_keywords)

if found_keywords:
    print("Se encontraron las siguientes palabras clave de politica:")
    for keyword in found_keywords:
        print(keyword)
else:
    print("No se encontraron palabras clave de politica en el texto.")
#Este código buscara las palabras clave de politica en un texto dado. Puedes ajustar las palabras clave de politica segun tus necesidades y aplicar este codigo a tus propios documentos o textos. Asegurate de proporcionar un texto real en lugar de sample_text para que la busqueda de politica sea efectiva.
