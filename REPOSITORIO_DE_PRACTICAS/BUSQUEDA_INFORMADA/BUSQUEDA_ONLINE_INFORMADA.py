import requests  # Importa la biblioteca requests para realizar solicitudes HTTP.
from bs4 import BeautifulSoup  # Importa BeautifulSoup para analizar el contenido HTML.

def buscar_en_linea(query):
    url = f"https://www.google.com/search?q={query}"  # Construye la URL de búsqueda en Google con la consulta proporcionada.
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        # Establece un encabezado de agente de usuario para simular una solicitud de un navegador web.
    }

    try:
        response = requests.get(url, headers=headers)  # Realiza una solicitud GET a la URL de búsqueda con el encabezado.
        response.raise_for_status()  # Verifica si la respuesta es exitosa.

        soup = BeautifulSoup(response.text, 'html.parser')  # Analiza el contenido HTML de la página de resultados.

        # Extraer los resultados de busqueda (títulos de los enlaces).
        resultados = soup.find_all("h3")  # Busca todos los elementos <h3> que contienen los títulos de los resultados.
        for i, resultado in enumerate(resultados, 1):
            print(f"{i}. {resultado.get_text()}")  # Imprime el número de resultado y su texto.

    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")  # Maneja errores relacionados con la solicitud HTTP.
    except Exception as e:
        print(f"Ocurrio un error: {e}")  # Maneja otros errores que puedan ocurrir.

if __name__ == "__main__":
    busqueda = input("Ingresa tu consulta: ")  # Solicita al usuario que ingrese la consulta de búsqueda.
    buscar_en_linea(busqueda)  # Llama a la funcion buscar_en_linea con la consulta ingresada por el usuario.