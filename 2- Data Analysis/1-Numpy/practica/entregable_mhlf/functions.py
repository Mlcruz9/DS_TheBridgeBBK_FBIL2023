import numpy as np
from variables import tablero

def colocar_barco(eslora):
    np.random.seed(45)
    coord_x_random = np.random.randint(10)
    coord_y_random = np.random.randint(10)
    print(coord_x_random)
    print(coord_y_random)
    orientacion = "O"
    print(orientacion)

    if orientacion == "E":

        tablero[coord_x_random, coord_y_random : coord_y_random + eslora] = "O"
        return tablero
    if orientacion == "O":
        tablero[coord_x_random, coord_y_random : coord_y_random - eslora] = "O"


def crear_tablero(size):
    tablero = np.full((size,size), " ")
    return tablero

def disparar():
    coor_jugador_x = int(input("Coordenada de disparo X: "))
    coor_jugador_y = int(input("Coordenada de disparo Y: "))

    if tablero[coor_jugador_x, coor_jugador_y] == "O":
        print("Has acertado! Dispara otra vez.")
        tablero[coor_jugador_x, coor_jugador_y] = "X"
        print(tablero)
    elif tablero[coor_jugador_x, coor_jugador_y] == " ":
        print("Has fallado! Turno de la máquina.")
        print(tablero)
        tablero[coor_jugador_x, coor_jugador_y] = "-"
    elif tablero[coor_jugador_x, coor_jugador_y] == "X" or tablero[coor_jugador_x, coor_jugador_y] == "-":
        print("Ya has usado esta coordenada previamente, intenta otra vez.")
        print(tablero)

tablero_jugador = crear_tablero(10)
