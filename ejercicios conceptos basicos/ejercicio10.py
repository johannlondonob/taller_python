# Mostrar promedio de notas
nota_es = float(input("Ingrese nota de ESPAÑOL: "))
nota_ma = float(input("Ingrese nota de MATEMÁTICAS: "))
nota_ec = float(input("Ingrese nota de ECONOMÍA: "))
nota_pr = float(input("Ingrese nota de PROGRAMACIÓN: "))
nota_in = float(input("Ingrese nota de INGLÉS: "))
promedio = (nota_es + nota_ma + nota_ec + nota_pr + nota_in) / 5
print(promedio)