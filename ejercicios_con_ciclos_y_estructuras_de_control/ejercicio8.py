# Mostrar la frecuencia de vocales en una frase
vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
frase = input("Ingresa una frase: ")
for index in frase:
    for vocal in vocales:
        if index == vocal:
            vocales[vocal] += 1
        else:
            pass
    else:
        pass
else:
    print(vocales)
