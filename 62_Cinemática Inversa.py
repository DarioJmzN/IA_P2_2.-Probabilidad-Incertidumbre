#Pablo Dario Jimenez Nu*o 21310143

import numpy as np

# Función para calcular la cinemática inversa de un brazo robótico de dos grados de libertad
def cinematica_inversa(x, y, l1, l2):
    q2 = np.arccos((x**2 + y**2 - l1**2 - l2**2) / (2 * l1 * l2))
    q1 = np.arctan2(y, x) - np.arctan2(l2 * np.sin(q2), l1 + l2 * np.cos(q2))
    return q1, q2

# Coordenadas objetivo
x_objetivo, y_objetivo = 3, 3

# Longitudes de los eslabones
l1, l2 = 2, 2

# Calcular la cinemática inversa
q1, q2 = cinematica_inversa(x_objetivo, y_objetivo, l1, l2)

# Mostrar los ángulos de las articulaciones
print("Ángulo de la articulación 1:", np.degrees(q1))
print("Ángulo de la articulación 2:", np.degrees(q2))







































