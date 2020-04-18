# Realice un algoritmo para generar e imprimir los números pares e impares que se encuentran entre 0 y 100. Además muestre la multiplicación de todos estos.
producto_pares, producto_impares, pares, impares = 1, 1, list(), list()
for i in range(2, 102, 2):
    pares.append(i)
    producto_pares *= i

for i in range(1, 100):
    if i % 3 == 0:
        impares.append(i)
        producto_impares *= i

print("Pares: ", pares)
print("Pares multiplicados: ", producto_pares)
print("Impares: ", impares)
print("Impares multiplicados: ", producto_impares)
