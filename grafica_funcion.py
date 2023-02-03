import math
import numpy as np
from matplotlib import pyplot as plt


# ejemplo de construcción de la gráfica para la función e^x

def funcionExponencial(x):
    return np.exp(x)


x = np.linspace(0, 10, 100) # los valores representan el inicio del grafico, o sea en x=0, luego el x=10 valor máximo en abscisa, y 100 es la catidad de puntos del gráfico
plt.plot(x, funcionExponencial(x))
plt.xlabel("x")  # nombre del eje x
plt.ylabel("e^x")  # nombre del eje y
plt.title(" Gráfico de la función exponencial") # título del gráfico
plt.grid() # para mostrar la cuadrícula


