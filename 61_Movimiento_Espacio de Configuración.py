#Pablo Dario Jimenez Nu*o 21310143

import matplotlib.pyplot as plt
import numpy as np

# Definir el rango de coordenadas x e y
x_range = np.linspace(0, 10, 100)
y_range = np.linspace(0, 10, 100)

# Crear una cuadrícula de coordenadas x e y
X, Y = np.meshgrid(x_range, y_range)

# Graficar el espacio de configuración
plt.figure(figsize=(6, 6))
plt.title('Espacio de Configuración de un Robot Móvil')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.grid(True)
plt.scatter(X, Y, s=1, color='blue')
plt.show()






































