# Eliminar todas las vocales encontradas en una frase y mostrar la cadena resultante
vocales, resultante = ["a", "e", "i", "o", "u"], ""
frase = input("Ingrese una frase: ")
for vocal in vocales:
    frase = frase.replace(vocal, "") 
print(frase)
