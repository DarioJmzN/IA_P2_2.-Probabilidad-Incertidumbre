#Pablo Dario Jimenez Nu*o 21310143

import numpy as np

# Posición verdadera del robot
x_verdadero = 0
y_verdadero = 0

# Desviación estándar de la incertidumbre en la posición
std_dev = 0.1

# Generar una muestra aleatoria de la posición del robot con incertidumbre
x_medido = np.random.normal(x_verdadero, std_dev)
y_medido = np.random.normal(y_verdadero, std_dev)

# Mostrar la posición medida del robot
print("Posición medida del robot (x, y):", x_medido, y_medido)








































