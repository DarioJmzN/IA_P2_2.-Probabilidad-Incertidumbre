#Pablo Dario Jimenez Nu*o 21310143

import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

# Generar datos de ejemplo
np.random.seed(0)
X = np.random.rand(100, 2)
y = np.random.randint(2, size=(100,))

# Definir el modelo de la red neuronal
model = Sequential([
    Dense(4, activation='relu', input_shape=(2,)),
    Dense(4, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compilar el modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X, y, epochs=100, verbose=0)

# Evaluar el modelo
loss, accuracy = model.evaluate(X, y)
print("Loss:", loss)
print("Accuracy:", accuracy)

# Predicciones
predictions = model.predict(X)
print("Predicciones:")
for i in range(len(X)):
    print("Entrada:", X[i], "| Predicción:", predictions[i][0])

















