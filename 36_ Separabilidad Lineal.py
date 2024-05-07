#Pablo Dario Jimenez Nu*o 21310143

import numpy as np
import matplotlib.pyplot as plt

# Generar datos de ejemplo
np.random.seed(0)
n_samples = 100
class_1 = np.random.randn(n_samples, 2) + [2, 2]
class_2 = np.random.randn(n_samples, 2) + [-2, -2]

# Visualizar los datos generados
plt.scatter(class_1[:, 0], class_1[:, 1], color='blue', label='Clase 1')
plt.scatter(class_2[:, 0], class_2[:, 1], color='red', label='Clase 2')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Datos Generados')
plt.legend()
plt.show()

# Verificar la separabilidad lineal
X = np.concatenate([class_1, class_2])
y = np.concatenate([np.ones(n_samples), -np.ones(n_samples)])

W = np.linalg.inv(X.T @ X) @ X.T @ y
y_pred = np.sign(X @ W)

if np.all(y_pred == y):
    print("Los datos son linealmente separables.")
else:
    print("Los datos no son linealmente separables.")
















