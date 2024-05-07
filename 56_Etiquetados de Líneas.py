#Pablo Dario Jimenez Nu*o 21310143

import cv2

# Leer la imagen
image = cv2.imread('image.jpg')

# Convertir la imagen a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar el umbral adaptativo para binarizar la imagen
binary_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)

# Encontrar los contornos en la imagen binarizada
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos en la imagen original
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Mostrar la imagen con los contornos dibujados
cv2.imshow('Image with Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


































