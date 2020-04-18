# Se requiere un algoritmo para obtener la estatura promedio de un grupo de personas, cuyo número de miembros se desconoce, el ciclo debe efectuarse siempre y cuando se tenga una estatura registrada.
estatura, suma_estatura, contador, promedio, centinela = 0, 0, 0, 0, True
while centinela:
    estatura = float(input("Ingrese estatura: "))
    contador += 1
    suma_estatura += estatura
    promedio = suma_estatura / contador
    centinela = int(
        input("¿Seguir? 1, para continuar; 0, para detenerse: ")) == 1
else:
    print(promedio)
