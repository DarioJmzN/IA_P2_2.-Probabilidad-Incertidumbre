# Pablo Dario Jimenez Nu*o 21310143

import numpy as np

class FiltroKalman:
    def __init__(self, A, B, H, Q, R):
        self.A = A  # Matriz de transición del estado
        self.B = B  # Matriz de control
        self.H = H  # Matriz de observación
        self.Q = Q  # Covarianza del proceso
        self.R = R  # Covarianza de la observación

        self.x_hat = None  # Estado estimado
        self.P = None      # Covarianza del estado estimado

    def inicializar(self, x0, P0):
        self.x_hat = x0  # Inicialización del estado estimado
        self.P = P0      # Inicialización de la covarianza del estado estimado

    def filtrar(self, u, z):
        # Predicción
        x_pred = np.dot(self.A, self.x_hat) + np.dot(self.B, u)
        P_pred = np.dot(np.dot(self.A, self.P), self.A.T) + self.Q

        # Actualización (corrección)
        y = z - np.dot(self.H, x_pred)
        S = np.dot(np.dot(self.H, P_pred), self.H.T) + self.R
        K = np.dot(np.dot(P_pred, self.H.T), np.linalg.inv(S))
        x_hat = x_pred + np.dot(K, y)
        P = P_pred - np.dot(np.dot(K, self.H), P_pred)

        # Actualizar el estado estimado y la covarianza
        self.x_hat = x_hat
        self.P = P

        return x_hat, P

    def predecir(self, u):
        # Predicción
        x_pred = np.dot(self.A, self.x_hat) + np.dot(self.B, u)
        P_pred = np.dot(np.dot(self.A, self.P), self.A.T) + self.Q

        return x_pred, P_pred

    def suavizar(self, estimaciones_filtradas):
        n = len(estimaciones_filtradas)
        estimaciones_suavizadas = []

        # Última estimación filtrada es la estimación inicial para el suavizado
        x_hat_suavizado = estimaciones_filtradas[-1][0]
        P_suavizado = estimaciones_filtradas[-1][1]

        estimaciones_suavizadas.append((x_hat_suavizado, P_suavizado))

        # Algoritmo de suavizado de Kalman recursivo
        for i in range(n - 2, -1, -1):
            x_pred = np.dot(self.A, estimaciones_filtradas[i][0])
            P_pred = np.dot(np.dot(self.A, estimaciones_filtradas[i][1]), self.A.T) + self.Q

            K = np.dot(np.dot(estimaciones_filtradas[i][1], self.A.T), np.linalg.inv(P_pred))
            x_hat_suavizado = estimaciones_filtradas[i][0] + np.dot(K, x_hat_suavizado - x_pred)
            P_suavizado = estimaciones_filtradas[i][1] + np.dot(np.dot(K, P_suavizado - P_pred), K.T)

            estimaciones_suavizadas.insert(0, (x_hat_suavizado, P_suavizado))

        return estimaciones_suavizadas

# Ejemplo de uso
# Definir matrices del modelo de espacio de estados
A = np.array([[1, 1], [0, 1]])  # Matriz de transición del estado
B = np.eye(2)  # Matriz de control
H = np.array([[1, 0]])  # Matriz de observación
Q = np.eye(2) * 0.1  # Covarianza del proceso
R = np.eye(1) * 1  # Covarianza de la observación

# Crear objeto FiltroKalman
filtro = FiltroKalman(A, B, H, Q, R)

# Inicializar filtro
x0 = np.array([0, 0])  # Estado inicial
P0 = np.eye(2) * 0.1  # Covarianza del estado inicial
filtro.inicializar(x0, P0)

# Datos de entrada (u: control, z: observación)
u = np.array([[0], [0]])
z = np.array([[1]])

# Filtrar
x_filtrado, P_filtrado = filtro.filtrar(u, z)
print("Estimación filtrada:")
print("Estado estimado:", x_filtrado)
print("Covarianza del estado estimado:", P_filtrado)

# Predecir
x_pred, P_pred = filtro.predecir(u)
print("\nEstimación predicha:")
print("Estado predicho:", x_pred)
print("Covarianza del estado predicho:", P_pred)

# Suavizar
estimaciones_filtradas = [(x_filtrado, P_filtrado)]
estimaciones_suavizadas = filtro.suavizar(estimaciones_filtradas)
print("\nEstimaciones suavizadas:")
for i, (x_hat_suavizado, P_suavizado) in enumerate(estimaciones_suavizadas):
    print(f"Paso {i+1}:")
    print("Estado estimado suavizado:", x_hat_suavizado)
    print("Covarianza del estado estimado suavizado:", P_suavizado)
















