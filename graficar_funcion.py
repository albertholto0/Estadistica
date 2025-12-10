from matplotlib import pyplot as plt
import numpy as np

# Solicitar al usuario la función
print("\nIngrese la función f(x) en formato lineal.")
print("Ejemplos: (2/3)*x**3-4*x**2+6*x  ---  sin(x)*exp(-0.2*x)  ---  2*sin(3*x)+0.5*x")
funcion = input("f(x) = ")

while True:
    # Solicitar al usuario el rango de la grafica
    print("\nIngrese el rango de la gráfica:")
    A = float(input("Ingrese el valor inicial A: "))
    B = float(input("Ingrese el valor final B: "))
    
    if A >= B:
        print("Error: El valor inicial A debe ser menor que el valor final B. Por favor, intente de nuevo.")
    else:
        break

# Generar el eje (x)
x = np.arange(A, B, 0.001)

# Diccionario de funciones matematicas permitidas
funciones_matematicas = {
    'sin': np.sin,
    'cos': np.cos,
    'tan': np.tan,
    'exp': np.exp,
    'log': np.log,
    'log10': np.log10,
    'sqrt': np.sqrt,
    'abs': np.abs,
    'arcsin': np.arcsin,
    'arccos': np.arccos,
    'arctan': np.arctan,
    'sinh': np.sinh,
    'cosh': np.cosh,
    'tanh': np.tanh,
    'pi': np.pi,
    'e': np.e,
    'floor': np.floor,
    'ceil': np.ceil,
    'sign': np.sign,
    'power': np.power,
    'cbrt': np.cbrt,
    'arcsinh': np.arcsinh,
    'arccosh': np.arccosh,
    'arctanh': np.arctanh,
    'degrees': np.degrees,
    'radians': np.radians
}

# Generar f(x) evaluando la función ingresada
fx = eval(funcion, funciones_matematicas | {'x': x})

# Generar la gráfica
fig = plt.figure()
fig.canvas.manager.set_window_title('Gráfica de la función')
plt.plot(x, fx, color='blue')
plt.legend()
plt.grid()
plt.title(f'Gráfica de la función {funcion}')
plt.show()  