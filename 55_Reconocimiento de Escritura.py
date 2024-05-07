#Pablo Dario Jimenez Nu*o 21310143

import cv2
import numpy as np

# Cargar el modelo pre-entrenado
net = cv2.dnn.readNet('mnist.onnx')

# Cargar las clases (dígitos del 0 al 9)
classes = [str(i) for i in range(10)]

# Leer la imagen de escritura a mano
image = cv2.imread('handwritten_digit.png', cv2.IMREAD_GRAYSCALE)

# Preprocesar la imagen
image = cv2.resize(image, (28, 28))
image = image.reshape(1, 1, 28, 28)
image = image.astype('float32')
image /= 255.0

# Establecer la entrada de la red neuronal
net.setInput(image)

# Realizar la predicción
output = net.forward()

# Obtener el índice de la clase predicha
predicted_class = np.argmax(output)

# Obtener la probabilidad de la clase predicha
confidence = output[0][predicted_class]

# Mostrar el resultado
print("El dígito reconocido es:", classes[predicted_class])
print("Confianza:", confidence)


































