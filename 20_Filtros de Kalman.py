#Pablo Dario Jimenez Nu*o 21310143

import numpy as np

class KalmanFilter:
    def __init__(self, F, H, Q, R, x0, P0):
        """
        Inicializa el filtro de Kalman.

        Args:
            F (numpy.ndarray): Matriz de transición de estado.
            H (numpy.ndarray): Matriz de observación.
            Q (numpy.ndarray): Covarianza del ruido de proceso.
            R (numpy.ndarray): Covarianza del ruido de medición.
            x0 (numpy.ndarray): Estado inicial.
            P0 (numpy.ndarray): Covarianza inicial.
        """
        self.F = F
        self.H = H
        self.Q = Q
        self.R = R
        self.x = x0
        self.P = P0

    def predict(self):
        """
        Predice el siguiente estado.
        """
        self.x = np.dot(self.F, self.x)
        self.P = np.dot(np.dot(self.F, self.P), self.F.T) + self.Q

    def update(self, z):
        """
        Actualiza el estado y la covarianza con una nueva observación.

        Args:
            z (numpy.ndarray): Nueva observación.
        """
        y = z - np.dot(self.H, self.x)
        S = np.dot(np.dot(self.H, self.P), self.H.T) + self.R
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))
        self.x = self.x + np.dot(K, y)
        self.P = np.dot((np.eye(len(self.x)) - np.dot(K, self.H)), self.P)

# Ejemplo de uso
F = np.array([[1, 1], [0, 1]])  # Matriz de transición de estado
H = np.array([[1, 0]])          # Matriz de observación
Q = np.array([[0.1, 0], [0, 0.1]])  # Covarianza del ruido de proceso
R = np.array([[1]])             # Covarianza del ruido de medición
x0 = np.array([0, 0])           # Estado inicial
P0 = np.eye(2)                  # Covarianza inicial

# Crear filtro de Kalman
kalman_filter = KalmanFilter(F, H, Q, R, x0, P0)

# Observaciones
observations = [1, 2, 3, 4, 5]

# Aplicar el filtro de Kalman
for z in observations:
    kalman_filter.predict()
    kalman_filter.update(np.array([z]))

    print("Predicción después de la observación {}: {}".format(z, kalman_filter.x))

