#Pablo Dario Jimenez Nu*o 21310143

import random

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mover(self):
        self.x += random.uniform(-1, 1)
        self.y += random.uniform(-1, 1)

# Crear un robot en una posición inicial
robot = Robot(0, 0)

# Realizar movimientos y actualizar la posición del robot
for _ in range(10):
    robot.mover()
    print("Posición actual del robot:", robot.x, robot.y)




































