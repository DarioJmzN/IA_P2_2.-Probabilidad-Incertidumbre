#Pablo Dario Jimenez Nu*o 21310143

import numpy as np

class HammingNetwork:
    def __init__(self, n_neurons):
        self.n_neurons = n_neurons
        self.weights = np.zeros((n_neurons, n_neurons))

    def train(self, patterns):
        self.weights = np.dot(patterns.T, patterns)
        np.fill_diagonal(self.weights, 0)

    def recall(self, input_pattern):
        output_pattern = np.dot(input_pattern, self.weights)
        output_pattern[output_pattern >= 0] = 1
        output_pattern[output_pattern < 0] = -1
        return output_pattern

# Ejemplo de uso
patterns = np.array([[1, 1, -1, -1], [-1, -1, 1, 1]])
network = HammingNetwork(n_neurons=4)
network.train(patterns)

input_pattern = np.array([-1, 1, -1, 1])
output_pattern = network.recall(input_pattern)
print("Entrada:", input_pattern)
print("Salida:", output_pattern)




















