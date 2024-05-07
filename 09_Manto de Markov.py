# Pablo Dario Jimenez Nu*o 21310143

import numpy as np

class ModeloMarkov:
    def __init__(self, matriz_transicion, estados):
        """
        Inicializa el modelo de Markov.

        Args:
        - matriz_transicion (numpy.ndarray): La matriz de transición del modelo.
        - estados (list): Una lista de los estados del modelo.
        """
        self.matriz_transicion = matriz_transicion
        self.estados = estados

    def calcular_probabilidad_estado_futuro(self, estado_actual, pasos_futuros):
        """
        Calcula la probabilidad de los estados futuros dados un estado inicial y un número de pasos futuros.

        Args:
        - estado_actual (str): El estado actual del sistema.
        - pasos_futuros (int): El número de pasos futuros para predecir.

        Returns:
        - dict: Un diccionario con la probabilidad de los estados futuros.
        """
        # Encuentra el índice del estado actual
        indice_estado_actual = self.estados.index(estado_actual)
        # Calcula la distribución de probabilidad del estado futuro
        distribucion_probabilidad = np.linalg.matrix_power(self.matriz_transicion, pasos_futuros)[indice_estado_actual]
        # Crea un diccionario con la probabilidad de los estados futuros
        probabilidad_estados_futuros = {estado: distribucion_probabilidad[i] for i, estado in enumerate(self.estados)}
        return probabilidad_estados_futuros

# Definimos la matriz de transición y los estados del modelo de Markov
matriz_transicion = np.array([[0.7, 0.2, 0.1],
                               [0.1, 0.6, 0.3],
                               [0.3, 0.1, 0.6]])
estados = ['Soleado', 'Nublado', 'Lluvioso']

# Creamos el modelo de Markov
modelo_markov = ModeloMarkov(matriz_transicion, estados)

# Calculamos la probabilidad de los estados futuros dado un estado actual y un número de pasos futuros
estado_actual = 'Soleado'
pasos_futuros = 2
probabilidad_estados_futuros = modelo_markov.calcular_probabilidad_estado_futuro(estado_actual, pasos_futuros)

# Imprimimos la probabilidad de los estados futuros
print("Probabilidad de l












