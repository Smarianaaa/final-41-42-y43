# Crear una matríz de 3 filas por 5 columnas con elementos de tipo int, cargar sus datos y luego imprimirlos.

import numpy as np

matriz = np.zeros((3,5), dtype=int)

for i in range(3):
    for j in range(5):
        matriz[i,j] = int(input("Ingrese un valor: "))

print(matriz)