# Se requiere un algoritmo para determinar, de N cantidades, cuántas son menores o iguales a cero y cuántas mayores a cero.

true, lista_mayores, lista_menores, numero = True, list(), list(), 0
while true:
    numero = int(input("Ingresa un número real: "))
    if numero > 0:
        lista_mayores.append(numero)
    else:
        lista_menores.append(numero)
    true = int(input("¿Seguir? 1, continuar; 0, detener: ")) == 1
else:
    print("Mayores: ", len(lista_mayores))
    print("Menores: ", len(lista_menores))
