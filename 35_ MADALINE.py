#Pablo Dario Jimenez Nu*o 21310143


import numpy as np

class Madaline:
    def __init__(self, n_inputs, n_outputs, learning_rate=0.1, n_iterations=100):
        self.n_inputs = n_inputs
        self.n_outputs = n_outputs
        self.weights = np.random.rand(n_inputs, n_outputs)
        self.bias = np.random.rand(n_outputs)
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations

    def activation_function(self, x):
        return x

    def predict(self, inputs):
        weighted_sum = np.dot(inputs, self.weights) + self.bias
        return self.activation_function(weighted_sum)

    def train(self, X, y):
        for _ in range(self.n_iterations):
            for inputs, target in zip(X, y):
                prediction = self.predict(inputs)
                error = target - prediction
                self.weights += 2 * self.learning_rate * np.outer(inputs, error)
                self.bias += 2 * self.learning_rate * error

# Ejemplo de uso
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[1, 0], [0, 1], [0, 1], [1, 0]])

madaline = Madaline(n_inputs=2, n_outputs=2)
madaline.train(X, y)

print("Pesos finales:", madaline.weights)
print("Sesgo final:", madaline.bias)

# Probando MADALINE entrenado
for inputs, target in zip(X, y):
    prediction = madaline.predict(inputs)
    print("Entradas:", inputs, "| Predicción:", prediction)















