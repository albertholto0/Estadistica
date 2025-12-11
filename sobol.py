import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import qmc

""""
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.qmc.Sobol.html
"""


def evaluarInput(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n <= 0:
                print("Por favor, ingresa un número entero positivo.")
                continue
            return n
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

n = evaluarInput("[n]: ")
# "d" es el numero de dimensiones
# "scramble=True" para mayor aleatoriedad
numeros_aleatorios = qmc.Sobol(d=2, scramble=True).random(n)
np.set_printoptions(precision=3, suppress=True)
print(numeros_aleatorios)

# Graficar los puntos
plt.scatter(numeros_aleatorios[:, 0], numeros_aleatorios[:, 1], s=20, alpha=0.6)
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Puntos generados con Sobol (n={n})')
plt.grid(True)
plt.axis('equal')
plt.show()