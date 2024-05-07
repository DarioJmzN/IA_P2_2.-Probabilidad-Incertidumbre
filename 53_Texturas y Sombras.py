#Pablo Dario Jimenez Nu*o 21310143

import cv2
import numpy as np

# Leer la imagen
image = cv2.imread('imagen.jpg')

# Convertir la imagen a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar un filtro de textura
texture_filter = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
textured_image = cv2.filter2D(gray_image, -1, texture_filter)

# Aplicar un filtro de sombra
shadow_filter = np.array([[1, 2, 1],
                          [0, 0, 0],
                          [-1, -2, -1]])
shadow_image = cv2.filter2D(gray_image, -1, shadow_filter)

# Mostrar las imágenes originales y procesadas
cv2.imshow('Original', image)
cv2.imshow('Textura', textured_image)
cv2.imshow('Sombra', shadow_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
































