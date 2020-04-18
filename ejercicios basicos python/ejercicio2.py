# Se requiere un algoritmo para obtener la suma de diez cantidades mediante la utilización de un ciclo for.
from random import randint

suma = 0
for i in range(1, 10):
    suma += randint(1, 100)
else:
    print(suma)
