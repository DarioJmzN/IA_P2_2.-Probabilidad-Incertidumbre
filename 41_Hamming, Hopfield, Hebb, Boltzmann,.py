#Pablo Dario Jimenez Nu*o 21310143

import numpy as np

class HopfieldNetwork:
    def __init__(self, n_neurons):
        self.n_neurons = n_neurons
        self.weights = np.zeros((n_neurons, n_neurons))

    def train(self, patterns):
        self.weights = np.dot(patterns.T, patterns)
        np.fill_diagonal(self.weights, 0)

    def recall(self, input_pattern):
        output_pattern = np.copy(input_pattern)
        while True:
            old_output_pattern = np.copy(output_pattern)
            output_pattern = np.sign(np.dot(self.weights, output_pattern))
            if np.array_equal(output_pattern, old_output_pattern):
                break
        return output_pattern

# Ejemplo de uso
patterns = np.array([[1, 1, -1, -1], [-1, -1, 1, 1]])
network = HopfieldNetwork(n_neurons=4)
network.train(patterns)

input_pattern = np.array([-1, 1, -1, 1])
output_pattern = network.recall(input_pattern)
print("Entrada:", input_pattern)
print("Salida:", output_pattern)





















