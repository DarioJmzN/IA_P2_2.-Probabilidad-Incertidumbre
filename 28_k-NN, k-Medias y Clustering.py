#Pablo Dario Jimenez Nu*o 21310143

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans

# Generar datos de ejemplo
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Visualizar los datos generados
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Datos Generados")
plt.show()

# k-NN (k-Nearest Neighbors)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)

# Predecir la clase de un nuevo punto
new_point = np.array([[0, 2]])
predicted_class = knn.predict(new_point)
print("Clase predicha para el punto {}: {}".format(new_point, predicted_class))

# k-Means
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

# Obtener las etiquetas de los grupos y los centroides
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# Visualizar los grupos y los centroides
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='*', s=200, label='Centroides')
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Agrupamiento k-Means")
plt.legend()
plt.show()







