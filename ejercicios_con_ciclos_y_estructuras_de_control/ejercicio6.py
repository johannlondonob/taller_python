# Reemplazar una letra por la posición en el abecedario
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
              "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
frase = input("Ingresa una frase: ").lower()
position, resultado, i = 0, "", ""
for letra in frase:
    if letra != " ":
        position = abecedario.index(letra) + 1
        resultado += str(position)
        i += str(letra) + "(" + str(position) + ") "
    else:
        resultado += " "
print(resultado, " --> ", i)
