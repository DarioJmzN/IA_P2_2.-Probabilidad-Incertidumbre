#Pablo Dario Jimenez Nu*o 21310143

import cv2

# Cargar la red neuronal pre-entrenada (YOLOv3)
net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')

# Cargar las clases
classes = []
with open('coco.names', 'r') as f:
    classes = f.read().splitlines()

# Cargar la imagen
image = cv2.imread('image.jpg')
height, width, _ = image.shape

# Convertir la imagen a un blob
blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)

# Establecer la entrada de la red neuronal
net.setInput(blob)

# Obtener las capas de salida de la red neuronal
output_layers_names = net.getUnconnectedOutLayersNames()
layer_outputs = net.forward(output_layers_names)

# Procesar las detecciones
for output in layer_outputs:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, f'{classes[class_id].upper()} {int(confidence * 100)}%', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# Mostrar la imagen con las detecciones
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

































