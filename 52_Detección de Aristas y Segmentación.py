#Pablo Dario Jimenez Nu*o 21310143

import cv2
import numpy as np

# Leer la imagen
image = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar el filtro de Canny para detección de bordes
edges = cv2.Canny(image, 100, 200)

# Aplicar la segmentación utilizando el algoritmo de umbralización
ret, thresholded = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Mostrar las imágenes originales y procesadas
cv2.imshow('Original', image)
cv2.imshow('Bordes detectados (Canny)', edges)
cv2.imshow('Imagen segmentada', thresholded)
cv2.waitKey(0)
cv2.destroyAllWindows()































