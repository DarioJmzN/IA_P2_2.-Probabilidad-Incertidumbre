#Pablo Dario Jimenez Nu*o 21310143
import numpy as np

def sigmoid(x):
    """
    Función de activación sigmoide.
    """
    return 1 / (1 + np.exp(-x))

def relu(x):
    """
    Función de activación ReLU (Rectified Linear Unit).
    """
    return np.maximum(0, x)

def tanh(x):
    """
    Función de activación tangente hiperbólica.
    """
    return np.tanh(x)

def softmax(x):
    """
    Función de activación softmax.
    """
    exp_x = np.exp(x - np.max(x))  # Para evitar el desbordamiento numérico
    return exp_x / np.sum(exp_x, axis=0)

# Ejemplo de uso
x = np.array([-1, 0, 1])

print("Sigmoide:", sigmoid(x))
print("ReLU:", relu(x))
print("Tanh:", tanh(x))
print("Softmax:", softmax(x))












