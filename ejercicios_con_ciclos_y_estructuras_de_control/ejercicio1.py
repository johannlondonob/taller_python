# Calcular promedio de notas
calificaciones = {"español": 10, "matematicas": 7,
                  "economia": 6, "programacion": 8.7, "ingles": 9}
suma_notas, numero_notas = 0, 0
for item in calificaciones:
    suma_notas += calificaciones[item]
    numero_notas += 1
else:
    promedio = suma_notas / numero_notas
    print(promedio)
