#Al jugar las coordenadas se escriben sin los parentesis
#Se asume que lo que ingrese el usuario va a ser correcto (no 
# va a poner coordenadas donde ya no hay cartas, coordenadas 
# que no existan o la misma coordenada dos veces), y que el 
#numero de cartas ingresado será valida (cant de cartas > 0)

import numpy as np
from tabulate import tabulate

######## GENERADOR DE CARTAS Y TABLEROS ########
def boards(number_of_cards):
    cards = []
    for i in range(1, number_of_cards + 1):
        cards.append(i)
        cards.append(i)
    np.random.shuffle(cards)

    columns = 5
    rows = (number_of_cards*2)/columns
    #Tablero con el valor de las cartas censurado
    board1 = []
    i = 0
    j = 0
    while j < rows:
        row = []
        k = 0
        while i < len(cards) and k < columns:
            f = str(j)
            c = str(k)
            row.append((j,k))
            i += 1
            k += 1
        board1.append(row)
        j += 1
    #Tablero que contiene las cartas con las cuales se
    #comparan las coordenadas ingresadas en el juego
    board2 = []
    i = 0
    j = 0
    while j < rows:
        row = []
        k = 0
        while i < len(cards) and k < columns:
            row.append(cards[i])
            i += 1
            k += 1
        board2.append(row)
        j += 1
    return board1, board2

################    JUEGO    ################
k = 0
points = {"Jugador 1":0, "Jugador 2":0 }
def game(board1,board2,k,points):
    players = ["Jugador 1", "Jugador 2"]
    turn = players[k]
    #Condicion para romper la recursividad de la funcion
    n = 0
    while n < len(board1):
        i = board1[n]
        if all(type(j) is str for j in i):
            n += 1 
            if n == len(board1):
                if points["Jugador 1"] > points["Jugador 2"]:
                    print("\n", "El ganador es: Jugador 1", "\n")
                else:
                    print("\n", "El ganador es: Jugador 2", "\n")
                return
        else:
            break

    print("\n","Juega: " , turn, "\n")

    print(tabulate(board1, tablefmt = 'fancy_grid'))

    c1 = input("Coordenadas primera carta: ")
    c = c1.split(',')
    x1 = int(c[0])
    y1 = int(c[1])
    board1[x1][y1] = board2[x1][y1]
    card1 = board2[x1][y1]

    print(tabulate(board1, tablefmt = 'fancy_grid'))

    c2 = input("Coordenadas segunda carta: ")
    c = c2.split(",")
    x2 = int(c[0])
    y2 = int(c[1])
    board1[x2][y2] = board2[x2][y2]
    card2 = board2[x2][y2]

    print(tabulate(board1, tablefmt = 'fancy_grid'))
    #Se compara el valor de ambas cartas y se define de quien
    #es el siguiente turno
    if card1 == card2:
        points[turn] = points[turn] + 1
        board1[x1][y1] = ""
        board1[x2][y2] = ""
        if k == 0:
            k = 0
        elif k == 1:
            k = 1   
    elif card1 != card2:
        board1[x1][y1] = ((x1,y1))
        board1[x2][y2] = ((x2,y2))
        if k == 0:
            k = 1
        elif k == 1:
            k = 0
    game(board1, board2, k, points)

##### LLAMADA DE LAS FUNCNIOINES PARA JUGAR #####
number_of_cards = int(input("Numero de cartas a jugar: "))
board1 = boards(number_of_cards)[0]
board2 = boards(number_of_cards)[1]
game(board1,board2,k,points)