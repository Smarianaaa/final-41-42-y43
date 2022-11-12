# Crear un programa que almacene los salarios de n empleados, el usuario debe ingresar la cantidad de sueldos a ingresar. Después de ingresarlos debe mostrar los salarios y el 5% de ISR que el empleado debe pagar.

import numpy as np
from prettytable import PrettyTable

n = int(input("Ingrese la cantidad de empleados: "))
salarios = np.zeros(n, dtype=float)

for i in range(n):
    salarios[i] = float(input("Ingrese el salario: "))

tabla = PrettyTable()
tabla.field_names = ["Salario", "ISR"]

for salario in salarios:
    tabla.add_row([salario, salario * 0.05])

print(tabla)