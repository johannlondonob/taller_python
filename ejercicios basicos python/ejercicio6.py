# Realice un algoritmo para generar N elementos de la sucesión de Fibonacci (0, 1, 1, 2, 3, 5, 8, 13, ...)
uno, dos, tres, tope, serie = 0, 1, 0, 0, list()
tope = int(input("Ingrese tope de serie: "))
while tope >= 0:
    tres = uno + dos
    uno, dos = dos, tres
    serie.append(tres)
    tope -= 1

print(serie)
