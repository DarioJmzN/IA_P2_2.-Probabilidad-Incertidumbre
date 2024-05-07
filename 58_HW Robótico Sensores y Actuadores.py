#Pablo Dario Jimenez Nu*o 21310143

class Sensor:
    def __init__(self):
        pass
    
    def leer_valor(self):
        # Simulación de lectura del sensor
        return 10

class Actuador:
    def __init__(self):
        pass
    
    def activar(self, valor):
        # Simulación de activación del actuador
        print("El actuador ha sido activado con valor:", valor)

# Crear un sensor y un actuador
sensor = Sensor()
actuador = Actuador()

# Leer el valor del sensor
valor_sensor = sensor.leer_valor()

# Activar el actuador con el valor leído del sensor
actuador.activar(valor_sensor)




































