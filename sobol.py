import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import qmc

""""
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.qmc.Sobol.html
"""


while True:
    try:
        n = int(input("Cantidad de puntos a generar [n]: "))
        if n <= 0:
            print("Por favor, ingresa un número entero positivo.")
            break
    except ValueError:
        print("Entrada inválida. Ingrese un número entero.")

# "d" es el numero de dimensiones
# "scramble=True" para mayor aleatoriedad
numeros_aleatorios = qmc.Sobol(d=2, scramble=True).random(n)

np.set_printoptions(precision=3, suppress=True)
print(numeros_aleatorios)

# Generacion de números aleatorios con Numpy, para comparar
numeros_aleatorios_np = np.random.rand(n, 2)

# Crear figura con dos subgráficas lado a lado
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Gráfica 1: Sobol
ax1.scatter(numeros_aleatorios[:, 0], numeros_aleatorios[:, 1], s=20, alpha=0.6, color='blue')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title(f'Sobol (n={n})')
ax1.grid(True)
ax1.axis('equal')

# Gráfica 2: NumPy random
ax2.scatter(numeros_aleatorios_np[:, 0], numeros_aleatorios_np[:, 1], s=20, alpha=0.6, color='red')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title(f'NumPy random (n={n})')
ax2.grid(True)
ax2.axis('equal')

plt.tight_layout()
plt.show()