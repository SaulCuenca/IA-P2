base_de_datos_peliculas = {
    "Pelicula1": ["Aventura", "Acci�n", "Ciencia Ficci�n"],
    "Pelicula2": ["Comedia", "Romance"],
    "Pelicula3": ["Drama", "Romance"],
    # ... M�s pel�culas ...
}

preferencias_usuario = {
    "Aventura": 5,
    "Acci�n": 4,
    "Romance": 3,
    # ... M�s preferencias ...
}

# Razonamiento: Recomendar pel�culas en funci�n de las preferencias del usuario.

def recomendar_peliculas(base_de_datos, preferencias, umbral=3):
    recomendaciones = []
    for pelicula, generos in base_de_datos.items():
        puntaje = 0
        for genero in generos:
            if genero in preferencias:
                puntaje += preferencias[genero]
        if puntaje >= umbral:
            recomendaciones.append(pelicula)
    return recomendaciones

# Llamada a la funci�n para obtener recomendaciones basadas en preferencias del usuario
recomendaciones = recomendar_peliculas(base_de_datos_peliculas, preferencias_usuario)

# Resultados: Imprimir las pel�culas recomendadas.
if recomendaciones:
    print("Pel�culas recomendadas:")
    for pelicula in recomendaciones:
        print(pelicula)
else:
    print("No se encontraron pel�culas recomendadas.")

# En este c�digo:
# - La base de datos de pel�culas y preferencias del usuario representa el conocimiento del sistema.
# - El razonamiento se realiza al calcular un puntaje para cada pel�cula en funci�n de las preferencias del usuario.
# - Las recomendaciones se generan a partir del razonamiento basado en las preferencias del usuario.
