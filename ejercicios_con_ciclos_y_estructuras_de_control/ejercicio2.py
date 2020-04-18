# Mostrar la calificación más alta
calificaciones = {"español": 10, "matematicas": 7,
                  "economia": 6, "programacion": 8.7, "ingles": 9}
mejor_nota = 0
for materia in calificaciones:
    if calificaciones[materia] >= mejor_nota:
        mejor_nota = calificaciones[materia]
    else:
        pass
else:
    print(mejor_nota)
