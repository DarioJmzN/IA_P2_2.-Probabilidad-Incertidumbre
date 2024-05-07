#Pablo Dario Jimenez Nu*o 21310143

import numpy as np

class NaiveBayes:
    def __init__(self):
        self.prior = None
        self.likelihood = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.classes = np.unique(y)
        n_classes = len(self.classes)

        self.prior = np.zeros(n_classes)
        self.likelihood = np.zeros((n_classes, n_features))

        for i, c in enumerate(self.classes):
            X_c = X[y == c]
            self.prior[i] = len(X_c) / n_samples
            self.likelihood[i, :] = (X_c.sum(axis=0) + 1) / (X_c.sum() + n_features)

    def predict(self, X):
        predictions = []
        for x in X:
            posterior = []
            for i, c in enumerate(self.classes):
                likelihood = np.prod(self.likelihood[i, :] ** x)
                posterior.append(likelihood * self.prior[i])
            predictions.append(self.classes[np.argmax(posterior)])
        return predictions

# Ejemplo de uso
X_train = np.array([[1, 1, 0], [1, 0, 0], [0, 1, 1], [0, 0, 1]])
y_train = np.array([0, 0, 1, 1])
X_test = np.array([[1, 1, 1], [0, 0, 0]])

# Crear y entrenar el clasificador Naïve Bayes
nb_classifier = NaiveBayes()
nb_classifier.fit(X_train, y_train)

# Predecir las clases de los datos de prueba
predictions = nb_classifier.predict(X_test)
print("Predicciones:", predictions)



