# Pablo Dario Jimenez Nu*o 21310143

import numpy as np

def proceso_markov(matriz_transicion, distribucion_inicial, n):
    """
    Realiza un proceso de Markov con una matriz de transición dada.

    Args:
    - matriz_transicion (np.ndarray): Una matriz de transición donde cada fila representa las probabilidades de transición
                                       desde un estado hacia todos los demás estados.
    - distribucion_inicial (np.ndarray): La distribución de probabilidad inicial sobre los estados.
    - n (int): El número de pasos en el proceso de Markov.

    Returns:
    - np.ndarray: La distribución de probabilidad final después de n pasos.
    """
    distribucion_actual = distribucion_inicial
    for _ in range(n):
        distribucion_actual = np.dot(distribucion_actual, matriz_transicion)

    return distribucion_actual

# Ejemplo de uso
matriz_transicion = np.array([[0.7, 0.3],
                               [0.4, 0.6]])
distribucion_inicial = np.array([0.5, 0.5])
n = 10

distribucion_final = proceso_markov(matriz_transicion, distribucion_inicial, n)
print("Distribución final después de", n, "pasos:", distribucion_final)
















