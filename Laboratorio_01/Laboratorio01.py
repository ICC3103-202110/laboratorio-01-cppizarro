import numpy as np

cant_cartas = int(input("Numero de cartas a jugar: "))

cartas = []
for i in range(1, cant_cartas + 1):
    cartas.append(i)
    cartas.append(i)

np.random.shuffle(cartas)