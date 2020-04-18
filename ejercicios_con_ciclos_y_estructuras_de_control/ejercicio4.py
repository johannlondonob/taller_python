# Mostrar palabras que ingrese un usuario siempre que sean palíndromos
seguir, cadena_original, cadena_copiada, lista = True, "", "", []
while seguir:
    cadena_original = input("Ingrese una palabra: ")
    cadena_copiada = cadena_original[::-1]
    if cadena_original == cadena_copiada:
        lista.append(cadena_copiada)
    else:
        pass

    seguir = int(float(input("¿Desea continuar? Presione 1 o 0: "))) == 1
else:
    print(lista)
