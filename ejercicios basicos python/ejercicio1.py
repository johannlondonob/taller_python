# Se requiere un algoritmo para obtener la edad promedio de un grupo de N alumnos. Si algún alumno tiene más de 18 años, se muestra el promedio que se lleva sin contar el alumno de 18 años. EL usuario decide si desea cerrar el programa o vuelve a ejecutarlo.

true, edad, suma_edad, promedio, contador = True, 0, 0, 0, 0
while true:
    contador += 1
    edad = int(input("Ingrese edad:"))
    suma_edad += edad
    promedio = suma_edad / contador
    if edad > 18:
        print(promedio)
    true = int(input("¿Seguir? 1, seguir; 0, detener programa: ")) == 1
else:
    print(promedio)
