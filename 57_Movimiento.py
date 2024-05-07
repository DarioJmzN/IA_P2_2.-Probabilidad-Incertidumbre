#Pablo Dario Jimenez Nu*o 21310143

import cv2

# Función para detectar movimiento en el video
def detect_motion(video_path):
    # Leer el video
    cap = cv2.VideoCapture(video_path)

    # Leer el primer frame
    _, prev_frame = cap.read()

    # Convertir el frame a escala de grises
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

    while True:
        # Leer el siguiente frame
        ret, next_frame = cap.read()
        if not ret:
            break

        # Convertir el frame a escala de grises
        next_gray = cv2.cvtColor(next_frame, cv2.COLOR_BGR2GRAY)

        # Calcular la diferencia absoluta entre los dos frames
        diff = cv2.absdiff(prev_gray, next_gray)

        # Aplicar un umbral para resaltar las áreas de cambio
        _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

        # Encontrar los contornos de las áreas de cambio
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Dibujar los contornos en el frame original
        for contour in contours:
            cv2.drawContours(next_frame, [contour], -1, (0, 255, 0), 2)

        # Mostrar el frame con los contornos dibujados
        cv2.imshow('Motion Detection', next_frame)

        # Actualizar el frame anterior
        prev_gray = next_gray

        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Liberar los recursos y cerrar las ventanas
    cap.release()
    cv2.destroyAllWindows()

# Ruta del video
video_path = 'video.mp4'

# Llamar a la función para detectar movimiento
detect_motion(video_path)



































