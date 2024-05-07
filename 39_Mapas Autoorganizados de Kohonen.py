#Pablo Dario Jimenez Nu*o 21310143

from minisom import MiniSom
import numpy as np
import matplotlib.pyplot as plt

# Generar datos de ejemplo
np.random.seed(0)
data = np.random.rand(100, 2)

# Definir el tamaño del SOM
som_width = 10
som_height = 10

# Inicializar y entrenar el SOM
som = MiniSom(som_width, som_height, 2, sigma=0.5, learning_rate=0.5)
som.train_random(data, 100)

# Obtener los pesos finales del SOM
weights = som.get_weights()

# Visualizar los pesos del SOM
plt.figure(figsize=(8, 8))
for i in range(som_width):
    for j in range(som_height):
        plt.plot(weights[i, j, 0], weights[i, j, 1], marker='o', markersize=8, color='b')
        if i < som_width - 1:
            plt.plot([weights[i, j, 0], weights[i + 1, j, 0]], [weights[i, j, 1], weights[i + 1, j, 1]], color='r')
        if j < som_height - 1:
            plt.plot([weights[i, j, 0], weights[i, j + 1, 0]], [weights[i, j, 1], weights[i, j + 1, 1]], color='r')
plt.title('Mapa Autoorganizado de Kohonen')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.grid()
plt.show()



















