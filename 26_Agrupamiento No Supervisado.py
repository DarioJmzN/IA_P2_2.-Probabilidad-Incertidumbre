#Pablo Dario Jimenez Nu*o 21310143

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Generar datos de ejemplo
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Visualizar los datos generados
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Datos Generados")
plt.show()

# Inicializar y ajustar el modelo K-Means
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
plt.title("Agrupamiento K-Means")
plt.legend()
plt.show()





