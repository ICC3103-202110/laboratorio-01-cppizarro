import numpy as np

cant_cartas = int(input("Numero de cartas a jugar: "))

cartas = []
for i in range(1, cant_cartas + 1):
    cartas.append(i)
    cartas.append(i)

np.random.shuffle(cartas)

print(cartas)

def tablero(cartas):
    
    tablero1 = np.matrix(['*']*5)
    tablero2 = np.matrix(['']*3)
    return tablero1, tablero2



#puntos = {jugdor1:0, jugador2:0}



# for i in range(cant_cartas):
#     tablero.append(["*"])

def juego():
    pass

# for d in lienzo:
#     print(*d, sep='')