# Pablo Dario Jimenez Nu*o 21310143

import numpy as np

class DistribucionProbabilidad:
    def __init__(self, valores, probabilidades):
        """
        Inicializa la distribución de probabilidad.

        Args:
        - valores (list): Una lista de valores posibles para la variable aleatoria.
        - probabilidades (list): Una lista de probabilidades correspondientes a los valores.
        """
        self.valores = valores
        self.probabilidades = probabilidades

    def media(self):
        """
        Calcula la media de la distribución de probabilidad.

        Returns:
        - float: La media de la distribución.
        """
        return np.sum(np.multiply(self.valores, self.probabilidades))

    def varianza(self):
        """
        Calcula la varianza de la distribución de probabilidad.

        Returns:
        - float: La varianza de la distribución.
        """
        media = self.media()
        return np.sum(np.multiply(np.square(self.valores - media), self.probabilidades))

# Ejemplo de distribución de probabilidad discreta
valores = [1, 2, 3, 4, 5]
probabilidades = [0.1, 0.2, 0.3, 0.2, 0.2]

# Creamos la distribución de probabilidad
distribucion = DistribucionProbabilidad(valores, probabilidades)

# Calculamos la media y la varianza
media = distribucion.media()
varianza = distribucion.varianza()

# Imprimimos los resultados
print("Valores:", valores)
print("Probabilidades:", probabilidades)
print("Media:", media)
print("Varianza:", varianza)


# Normalizamos las probabilidades
probabilidades = [0.3, 0.2, 0.5]
probabilidades_normalizadas = normalizar_probabilidades(probabilidades)
print("Probabilidades normalizadas:", probabilidades_normalizadas)
print("Suma de las probabilidades normalizadas:", sum(probabilidades_normalizadas))










