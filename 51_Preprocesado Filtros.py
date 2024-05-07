#Pablo Dario Jimenez Nu*o 21310143

import matplotlib.pyplot as plt

from sklearn import preprocessing
import numpy as np

# Datos de ejemplo
data = np.array([[1, 2], [2, 4], [3, 6]])

# Escalar los datos
scaler = preprocessing.StandardScaler()
scaled_data = scaler.fit_transform(data)

# Mostrar los datos originales y escalados
print("Datos originales:")
print(data)
print("\nDatos escalados:")
print(scaled_data)






























