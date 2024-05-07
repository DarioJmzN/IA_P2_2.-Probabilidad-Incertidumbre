#Pablo Dario Jimenez Nu*o 21310143

from hmmlearn import hmm
import numpy as np

# Definir el modelo HMM
model = hmm.MultinomialHMM(n_components=2)  # 2 estados ocultos

# Parámetros del modelo
model.startprob_ = np.array([0.5, 0.5])  # Probabilidades iniciales de los estados ocultos
model.transmat_ = np.array([[0.7, 0.3],   # Matriz de transición de los estados ocultos
                            [0.4, 0.6]])
model.emissionprob_ = np.array([[0.9, 0.1], # Probabilidades de emisión de los estados observables
                                [0.2, 0.8]])

# Generar secuencia de observaciones
X, Z = model.sample(n_samples=100)

# Ajustar el modelo a los datos observados
model.fit(X)

# Predecir el estado oculto y la secuencia de observaciones
hidden_states = model.predict(X)
predicted_observations = model.predict_proba(X)

print("Secuencia de estados ocultos predichos:")
print(hidden_states)

print("\nSecuencia de observaciones predichas:")
print(predicted_observations)






