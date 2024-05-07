#Pablo Dario Jimenez Nu*o 21310143

import numpy as np

# Definir una trayectoria objetivo
trayectoria_x = np.linspace(0, 10, 100)
trayectoria_y = np.sin(trayectoria_x)

# Controlador de seguimiento de trayectoria
def controlador_seguimiento(trayectoria_x, trayectoria_y, robot_x, robot_y):
    # Calcular el error de seguimiento de la trayectoria
    error_x = trayectoria_x - robot_x
    error_y = trayectoria_y - robot_y
    
    # Aplicar un control proporcional para ajustar la velocidad del robot
    velocidad_lineal = 0.5 * error_x
    velocidad_angular = 0.1 * error_y
    
    return velocidad_lineal, velocidad_angular

# Posición actual del robot
robot_x = 0
robot_y = 0

# Controlar el robot para seguir la trayectoria
for i in range(len(trayectoria_x)):
    vl, va = controlador_seguimiento(trayectoria_x[i], trayectoria_y[i], robot_x, robot_y)
    print("Velocidad lineal:", vl, "Velocidad angular:", va)









































