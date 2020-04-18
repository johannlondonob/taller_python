# Mostrar cantidad de vocales ingresadas en una frase
vocales, contador_vocales = ["a", "e", "i", "o", "u"], 0
frase = input("Ingresa una frase: ")
for vocal in vocales:
    contador_vocales += frase.count(vocal)
else:
    print(contador_vocales)