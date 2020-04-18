""" Almacenar 10 número positivos:
-> Mostrar la suma de todos ellos
-> Mostrar el promedio
-> El número mayor de ellos
-> El número menor de ellos
"""
almacen, suma, promedio, mayor, menor = [], 0, 0, 0, 99999999999999999

while almacen.__len__() < 10:
    n = float(input("Ingrese un número"))
    if n < 0:
        print("Debe ingresar números mayores que cero\n")
        pass
    else:
        almacen.append(n)
        suma += n
        if n >= mayor:
            mayor = n
        else:
            pass
        if n <= menor:
            menor = n
        else:
            pass
else:
    promedio = suma / almacen.__len__()
    print(almacen)
    print("Suma:", suma)
    print("Promedio: ", promedio)
    print("Cifra mayor: ", mayor)
    print("Cifra menor:", menor)
