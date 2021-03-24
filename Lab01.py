import numpy as np

cant_cartas = int(input("Numero de cartas a jugar: "))

cartas = []
for i in range(1, cant_cartas + 1):
    cartas.append(i)
    cartas.append(i)

np.random.shuffle(cartas)

print(cartas)

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

##############################################################