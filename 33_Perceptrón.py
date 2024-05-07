#Pablo Dario Jimenez Nu*o 21310143


import numpy as np

class Perceptron:
    def __init__(self, n_inputs, learning_rate=0.1, n_iterations=100):
        self.weights = np.random.rand(n_inputs)
        self.bias = np.random.rand()
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations

    def activation_function(self, x):
        return 1 if x >= 0 else 0

    def predict(self, inputs):
        weighted_sum = np.dot(inputs, self.weights) + self.bias
        return self.activation_function(weighted_sum)

    def train(self, X, y):
        for _ in range(self.n_iterations):
            for inputs, target in zip(X, y):
                prediction = self.predict(inputs)
                error = target - prediction
                self.weights += self.learning_rate * error * inputs
                self.bias += self.learning_rate * error

# Ejemplo de uso
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])

perceptron = Perceptron(n_inputs=2)
perceptron.train(X, y)

print("Pesos finales:", perceptron.weights)
print("Sesgo final:", perceptron.bias)

# Probando el perceptrón entrenado
for inputs, target in zip(X, y):
    prediction = perceptron.predict(inputs)
    print("Entradas:", inputs, "| Predicción:", prediction)













