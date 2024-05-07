#Pablo Dario Jimenez Nu*o 21310143

import numpy as np

def hacia_delante(transiciones, emisiones, inicial, observaciones):
    """
    Realiza el algoritmo de Hacia Delante para calcular la probabilidad de una secuencia de observaciones.

    Args:
    - transiciones (np.ndarray): Matriz de transiciones entre estados.
    - emisiones (np.ndarray): Matriz de emisiones de observaciones desde estados.
    - inicial (np.ndarray): Distribución de probabilidad inicial sobre los estados.
    - observaciones (list): Secuencia de observaciones.

    Returns:
    - float: La probabilidad de la secuencia de observaciones dada el modelo.
    """
    T = len(observaciones)  # Número de observaciones
    N = len(inicial)        # Número de estados

    # Inicializar matriz de avance
    forward = np.zeros((N, T))

    # Paso hacia delante
    forward[:, 0] = inicial * emisiones[:, observaciones[0]]
    for t in range(1, T):
        for j in range(N):
            forward[j, t] = np.sum(forward[:, t-1] * transiciones[:, j]) * emisiones[j, observaciones[t]]

    # Probabilidad de la secuencia de observaciones
    probabilidad = np.sum(forward[:, -1])

    return probabilidad, forward

def hacia_atras(transiciones, emisiones, observaciones):
    """
    Realiza el algoritmo de Hacia Atrás para calcular la probabilidad de una secuencia de observaciones.

    Args:
    - transiciones (np.ndarray): Matriz de transiciones entre estados.
    - emisiones (np.ndarray): Matriz de emisiones de observaciones desde estados.
    - observaciones (list): Secuencia de observaciones.

    Returns:
    - np.ndarray: La probabilidad de estar en un estado en un tiempo dado, dado el modelo y las observaciones.
    """
    T = len(observaciones)  # Número de observaciones
    N = transiciones.shape[0]  # Número de estados

    # Inicializar matriz de atrás
    backward = np.zeros((N, T))

    # Paso hacia atrás
    backward[:, -1] = 1
    for t in range(T - 2, -1, -1):
        for i in range(N):
            backward[i, t] = np.sum(backward[:, t+1] * transiciones[i, :] * emisiones[:, observaciones[t+1]])

    return backward

# Ejemplo de uso
# Definir modelo oculto de Markov (HMM)
transiciones = np.array([[0.7, 0.3], [0.4, 0.6]])  # Matriz de transiciones entre estados
emisiones = np.array([[0.9, 0.1], [0.2, 0.8]])      # Matriz de emisiones de observaciones desde estados
inicial = np.array([0.5, 0.5])                     # Distribución de probabilidad inicial sobre los estados
observaciones = [0, 1, 0]                           # Secuencia de observaciones

# Hacia Delante
probabilidad_forward, forward = hacia_delante(transiciones, emisiones, inicial, observaciones)
print("Probabilidad de la secuencia de observaciones (Hacia Delante):", probabilidad_forward)

# Hacia Atrás
backward = hacia_atras(transiciones, emisiones, observaciones)
print("\nProbabilidad de estar en un estado en un tiempo dado (Hacia Atrás):")
print(backward)
