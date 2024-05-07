#Pablo Dario Jimenez Nu*o 21310143

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import SVC

# Generar datos de ejemplo
X, y = datasets.make_circles(n_samples=100, factor=0.5, noise=0.1)

# Visualizar los datos generados
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Datos Generados")
plt.show()

# Crear y entrenar un clasificador SVM con núcleo RBF
svm_classifier = SVC(kernel='rbf', C=1, gamma='auto')
svm_classifier.fit(X, y)

# Visualizar la frontera de decisión
def plot_decision_boundary(X, y, classifier):
    h = 0.02  # Step size en la malla
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.3, cmap='viridis')
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')

# Visualizar la frontera de decisión del clasificador SVM
plt.figure()
plot_decision_boundary(X, y, svm_classifier)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Frontera de Decisión SVM con Núcleo RBF")
plt.show()








