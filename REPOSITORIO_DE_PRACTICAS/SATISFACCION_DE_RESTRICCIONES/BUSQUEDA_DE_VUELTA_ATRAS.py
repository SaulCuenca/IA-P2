def backtracking_search(maze, start, end):
    def is_valid(x, y):
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
            return True
        return False

    def solve(x, y):
        if x == end[0] and y == end[1]:
            return True

        if is_valid(x, y):
            maze[x][y] = 2  # Marcar como visitado

            # Movimientos posibles: arriba, abajo, izquierda, derecha
            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for move in moves:
                new_x, new_y = x + move[0], y + move[1]
                if solve(new_x, new_y):
                    return True

            # Si ningun movimiento conduce a la solucion, retroceder
            maze[x][y] = 0  # Desmarcar como no visitado
            return False

        return False

    if solve(start[0], start[1]):
        return maze
    else:
        return None

# Ejemplo de uso
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

result = backtracking_search(maze, start, end)

if result:
    print("Ruta encontrada:")
    for row in result:
        print(row)
else:
    print("No se encontro una ruta.")
#Este codigo utiliza la busqueda de vuelta atras para encontrar una ruta desde un punto de inicio hasta un punto de destino en un laberinto representado como una matriz bidimensional. Las celdas con valor 0 son caminos transitables, las celdas con valor 1 son obstaculos, y las celdas con valor 2 representan el camino de la solución encontrada.
#Asegurate de que la estructura de datos del problema que estás resolviendo se adapte a este codigo y modifica los valores y las reglas según sea necesario.
