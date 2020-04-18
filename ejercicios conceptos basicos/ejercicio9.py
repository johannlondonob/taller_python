# Meses transcurridos desde el nacimiento hasta el mes actual
from datetime import date

fecha_actual = date.today()
on = True
while on:
    anio_nacido = int(float(input("Año en que nació: ")))
    mes_nacido = int(float(input("Del 1 al 12, ingrese el mes en el que nació:\n\n ")))
    if mes_nacido >= 12:
        print("Ingresa un número dentro del rango: del 1 al 12")
        on = True
    else:
        meses_transcurridos = ((fecha_actual.year - anio_nacido) * 12) + (fecha_actual.month - mes_nacido)
        on = False
else:
    print(meses_transcurridos)
