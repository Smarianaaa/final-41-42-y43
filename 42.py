# Definir un vector de n posiciones en los que se pueda almacenar la altura de n personas en metros
# - El usuario debe ingresar la cantidad de personas a ingresar
# - Al final debe mostrar todas las alturas y la altura promedio

import numpy as np
from prettytable import PrettyTable

n = int(input("Ingrese la cantidad de personas: "))
alturas = np.zeros(n, dtype=float)

for i in range(n):
    alturas[i] = float(input("Ingrese la altura: "))

tabla = PrettyTable()
tabla.field_names = ["Altura", "Promedio"]

suma = 0
for altura in alturas:
    tabla.add_row([altura, ''])
    suma += altura

promedio = suma / n
tabla.add_row(['', promedio])
print(tabla)