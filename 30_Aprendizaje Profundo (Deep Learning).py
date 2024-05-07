#Pablo Dario Jimenez Nu*o 21310143

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

# Datos de ejemplo (puertas lógicas AND)
X = tf.constant([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=tf.float32)
y = tf.constant([[0], [0], [0], [1]], dtype=tf.float32)

# Definir el modelo de la red neuronal
model = Sequential([
    Dense(2, activation='relu', input_shape=(2,)),
    Dense(1, activation='sigmoid')
])

# Compilar el modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X, y, epochs=1000, verbose=0)

# Evaluar el modelo
loss, accuracy = model.evaluate(X, y)
print("Loss:", loss)
print("Accuracy:", accuracy)

# Predicciones
predictions = model.predict(X)
print("Predicciones:")
for i in range(len(X)):
    print("Entrada:", X[i].numpy(), "| Predicción:", predictions[i][0])










