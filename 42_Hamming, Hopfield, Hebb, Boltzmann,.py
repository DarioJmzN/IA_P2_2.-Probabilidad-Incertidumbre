#Pablo Dario Jimenez Nu*o 21310143

import numpy as np

class HebbianRule:
    def __init__(self, n_neurons):
        self.n_neurons = n_neurons
        self.weights = np.zeros((n_neurons, n_neurons))

    def train(self, patterns):
        for pattern in patterns:
            self.weights += np.outer(pattern, pattern)

    def recall(self, input_pattern):
        output_pattern = np.sign(np.dot(input_pattern, self.weights))
        return output_pattern

# Ejemplo de uso
patterns = np.array([[1, 1, -1, -1], [-1, -1, 1, 1]])
network = HebbianRule(n_neurons=4)
network.train(patterns)

input_pattern = np.array([-1, 1, -1, 1])
output_pattern = network.recall(input_pattern)
print("Entrada:", input_pattern)
print("Salida:", output_pattern)





















