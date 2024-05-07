#Pablo Dario Jimenez Nu*o 21310143

import numpy as np
from scipy.stats import multivariate_normal

class GaussianMixtureModel:
    def __init__(self, n_components, max_iter=100, tol=1e-4):
        self.n_components = n_components
        self.max_iter = max_iter
        self.tol = tol

    def fit(self, X):
        n_samples, n_features = X.shape

        # Inicialización aleatoria de medias y covarianzas
        np.random.seed(42)
        self.means = np.random.rand(self.n_components, n_features)
        self.covs = np.array([np.eye(n_features)] * self.n_components)
        self.weights = np.ones(self.n_components) / self.n_components

        for _ in range(self.max_iter):
            # E-step: Calcular las responsabilidades de cada componente para cada dato
            responsibilities = self._compute_responsibilities(X)

            # Guardar los parámetros anteriores
            old_means = np.copy(self.means)
            old_covs = np.copy(self.covs)
            old_weights = np.copy(self.weights)

            # M-step: Actualizar los parámetros
            self._update_parameters(X, responsibilities)

            # Calcular la diferencia entre los parámetros anteriores y los nuevos
            diff_means = np.linalg.norm(self.means - old_means)
            diff_covs = np.linalg.norm(self.covs - old_covs)
            diff_weights = np.linalg.norm(self.weights - old_weights)

            # Verificar convergencia
            if diff_means < self.tol and diff_covs < self.tol and diff_weights < self.tol:
                break

    def _compute_responsibilities(self, X):
        responsibilities = np.zeros((len(X), self.n_components))
        for i in range(self.n_components):
            responsibilities[:, i] = self.weights[i] * multivariate_normal.pdf(X, mean=self.means[i], cov=self.covs[i])
        responsibilities /= responsibilities.sum(axis=1, keepdims=True)
        return responsibilities

    def _update_parameters(self, X, responsibilities):
        # Actualizar pesos
        self.weights = responsibilities.mean(axis=0)

        # Actualizar medias
        self.means = np.dot(responsibilities.T, X) / responsibilities.sum(axis=0, keepdims=True)

        # Actualizar covarianzas
        for i in range(self.n_components):
            diff = X - self.means[i]
            self.covs[i] = np.dot(responsibilities[:, i] * diff.T, diff) / responsibilities[:, i].sum()

# Ejemplo de uso
X = np.random.randn(1000, 2)
X[:500, :] += 3
X[500:, :] -= 3

gmm = GaussianMixtureModel(n_components=2)
gmm.fit(X)

print("Pesos:", gmm.weights)
print("Medias:", gmm.means)
print("Covarianzas:", gmm.covs)




