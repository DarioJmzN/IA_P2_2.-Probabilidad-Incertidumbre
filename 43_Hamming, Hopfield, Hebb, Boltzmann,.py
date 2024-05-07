#Pablo Dario Jimenez Nu*o 21310143

import numpy as np

class BoltzmannMachine:
    def __init__(self, n_neurons):
        self.n_neurons = n_neurons
        self.weights = np.zeros((n_neurons, n_neurons))

    def train(self, patterns, learning_rate=0.1, epochs=100):
        for _ in range(epochs):
            for pattern in patterns:
                for i in range(self.n_neurons):
                    for j in range(self.n_neurons):
                        if i != j:
                            self.weights[i, j] += learning_rate * pattern[i] * pattern[j]

    def recall(self, input_pattern, n_iterations=100):
        output_pattern = np.copy(input_pattern)
        for _ in range(n_iterations):
            i = np.random.randint(self.n_neurons)
            output_pattern[i] = np.sign(np.dot(self.weights[i], output_pattern))
        return output_pattern

# Ejemplo de uso
patterns = np.array([[1, 1, -1, -1], [-1, -1, 1, 1]])
network = BoltzmannMachine(n_neurons=4)
network.train(patterns)

input_pattern = np.array([-1, 1, -1, 1])
output_pattern = network.recall(input_pattern)
print("Entrada:", input_pattern)
print("Salida:", output_pattern)






















