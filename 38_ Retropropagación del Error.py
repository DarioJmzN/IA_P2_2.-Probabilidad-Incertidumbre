#Pablo Dario Jimenez Nu*o 21310143

import numpy as np

class NeuralNetwork:
    def __init__(self, n_inputs, n_hidden, n_output, learning_rate=0.1):
        # Inicializar los pesos con valores aleatorios
        self.weights_input_hidden = np.random.rand(n_inputs, n_hidden)
        self.weights_hidden_output = np.random.rand(n_hidden, n_output)
        self.learning_rate = learning_rate

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward_propagation(self, inputs):
        # Calcular la salida de la capa oculta
        hidden_inputs = np.dot(inputs, self.weights_input_hidden)
        hidden_outputs = self.sigmoid(hidden_inputs)

        # Calcular la salida final
        final_inputs = np.dot(hidden_outputs, self.weights_hidden_output)
        final_outputs = self.sigmoid(final_inputs)

        return hidden_outputs, final_outputs

    def backward_propagation(self, inputs, target, hidden_outputs, final_outputs):
        # Calcular el error de la capa de salida
        output_errors = target - final_outputs
        output_delta = output_errors * self.sigmoid_derivative(final_outputs)

        # Calcular el error de la capa oculta
        hidden_errors = np.dot(output_delta, self.weights_hidden_output.T)
        hidden_delta = hidden_errors * self.sigmoid_derivative(hidden_outputs)

        # Actualizar los pesos
        self.weights_hidden_output += np.dot(hidden_outputs.T, output_delta) * self.learning_rate
        self.weights_input_hidden += np.dot(inputs.T, hidden_delta) * self.learning_rate

    def train(self, X, y, epochs):
        for epoch in range(epochs):
            for inputs, target in zip(X, y):
                hidden_outputs, final_outputs = self.forward_propagation(inputs)
                self.backward_propagation(inputs, target, hidden_outputs, final_outputs)

# Ejemplo de uso
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Crear y entrenar la red neuronal
nn = NeuralNetwork(n_inputs=2, n_hidden=4, n_output=1)
nn.train(X, y, epochs=1000)

# Realizar predicciones
print("Predicciones:")
for inputs in X:
    _, prediction = nn.forward_propagation(inputs)
    print("Entrada:", inputs, "| Predicción:", prediction[0])


















