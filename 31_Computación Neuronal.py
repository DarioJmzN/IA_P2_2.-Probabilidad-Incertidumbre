#Pablo Dario Jimenez Nu*o 21310143

import numpy as np

class Neuron:
    def __init__(self, n_inputs):
        # Inicializar los pesos y el sesgo de manera aleatoria
        self.weights = np.random.rand(n_inputs)
        self.bias = np.random.rand()

    def forward(self, inputs):
        # Calcular la suma ponderada de las entradas y aplicar la función de activación
        weighted_sum = np.dot(inputs, self.weights) + self.bias
        activation = self.activation_function(weighted_sum)
        return activation

    def activation_function(self, x):
        # Función de activación (en este caso, una función sigmoide)
        return 1 / (1 + np.exp(-x))

# Ejemplo de uso
n_inputs = 3
neuron = Neuron(n_inputs)

inputs = np.array([0.5, 0.3, 0.8])
output = neuron.forward(inputs)

print("Entradas:", inputs)
print("Salida de la neurona:", output)











