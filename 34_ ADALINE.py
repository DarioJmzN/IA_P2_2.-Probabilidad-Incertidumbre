#Pablo Dario Jimenez Nu*o 21310143


import numpy as np

class Adaline:
    def __init__(self, n_inputs, learning_rate=0.1, n_iterations=100):
        self.weights = np.random.rand(n_inputs)
        self.bias = np.random.rand()
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
                self.weights += 2 * self.learning_rate * error * inputs
                self.bias += 2 * self.learning_rate * error

# Ejemplo de uso
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])

adaline = Adaline(n_inputs=2)
adaline.train(X, y)

print("Pesos finales:", adaline.weights)
print("Sesgo final:", adaline.bias)

# Probando ADALINE entrenado
for inputs, target in zip(X, y):
    prediction = adaline.predict(inputs)
    print("Entradas:", inputs, "| Predicción:", prediction)














