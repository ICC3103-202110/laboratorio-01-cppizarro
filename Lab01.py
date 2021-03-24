import numpy as np

cant_cartas = int(input("Numero de cartas a jugar: "))

cartas = []
for i in range(1, cant_cartas + 1):
    cartas.append(i)
    cartas.append(i)

np.random.shuffle(cartas)

tablero1 = []
tablero2 = []

columnas = 4
filas = (cant_cartas*2)/columnas

i = 0
j = 0
while j < filas:
    fila = []
    k = 0
    while i < len(cartas) and k < columnas:
        f = str(j)
        c = str(k)
        fila.append((j,k))
        i += 1
        k += 1
    tablero1.append(fila)
    j += 1

i = 0
j = 0
while j < filas:
    fila = []
    k = 0
    while i < len(cartas) and k < columnas:
        fila.append(cartas[i])
        i += 1
        k += 1
    tablero2.append(fila)
    j += 1

#################################################

k = 0
puntos = {"Jugador 1":0, "Jugador 2":0 }
def juego(tablero1,tablero2,k,puntos):
    jugadores = ["Jugador 1", "Jugador 2"]
    turno = jugadores[k]
    n = 0
    while n < len(tablero1):
        i = tablero1[n]
        if all(type(j) is str for j in i):
            print(puntos)
            if puntos["Jugador 1"] > puntos["Jugador 2"]:
                print("El ganador es Jugador 1")
            else:
                print("El ganador es Jugador 2")
            n += 1
            if n == len(tablero1):
                return
        else:
            break
                    
    print('\n',"Juega: " , turno, '\n')

    for i in tablero1:
        print(*i)

    c1 = input("Coordenadas: ")
    c = c1.split(',')
    x1 = int(c[0])
    y1 = int(c[1])
    tablero1[x1][y1] = tablero2[x1][y1]
    carta1 = tablero2[x1][y1]

    for i in tablero1:
        print(*i)

    c2 = input("Coordenadas: ")
    c = c2.split(",")
    x2 = int(c[0])
    y2 = int(c[1])
    tablero1[x2][y2] = tablero2[x2][y2]
    carta2 = tablero2[x2][y2]

    for i in tablero1:
        print(*i)

    if carta1 == carta2:
        puntos[turno] = puntos[turno] + 1
        tablero1[x1][y1] = "    "
        tablero1[x2][y2] = "    "
        if k == 0:
            k = 0
        elif k == 1:
            k = 1
        juego(tablero1, tablero2, k, puntos)
        
    if carta1 != carta2:
        tablero1[x1][y1] = ((x1,y1))
        tablero1[x2][y2] = ((x2,y2))
        if k == 0:
            k = 1
        elif k == 1:
            k = 0
        juego(tablero1, tablero2, k, puntos)
    

print(tablero2)
juego(tablero1,tablero2,k,puntos)

#MEJORAR COMO SE VE CUANDO SE IMPRIME