#Pablo Dario Jimenez Nu*o 21310143

class Robot:
    def __init__(self, nombre, x=0, y=0, orientacion=0):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.orientacion = orientacion
    
    def mover_adelante(self, distancia):
        self.x += distancia * cos(self.orientacion)
        self.y += distancia * sin(self.orientacion)
    
    def girar(self, angulo):
        self.orientacion += angulo
    
    def obtener_posicion(self):
        return self.x, self.y
    
    def obtener_orientacion(self):
        return self.orientacion

# Crear un robot llamado "MiRobot"
MiRobot = Robot("MiRobot")

# Mover el robot hacia adelante
MiRobot.mover_adelante(5)

# Girar el robot
MiRobot.girar(pi/2)

# Obtener la posición y orientación actual del robot
posicion_actual = MiRobot.obtener_posicion()
orientacion_actual = MiRobot.obtener_orientacion()

print("Posición actual:", posicion_actual)
print("Orientación actual:", orientacion_actual)










































