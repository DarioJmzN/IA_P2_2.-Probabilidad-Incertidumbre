#Pablo Dario Jimenez Nu*o 21310143

class Mapa:
    def __init__(self):
        self.landmarks = {}
    
    def agregar_landmark(self, x, y):
        landmark_id = len(self.landmarks) + 1
        self.landmarks[landmark_id] = (x, y)
        return landmark_id

# Crear un mapa
mapa = Mapa()

# Agregar landmarks al mapa
mapa.agregar_landmark(1, 1)
mapa.agregar_landmark(2, 3)
mapa.agregar_landmark(4, 2)

# Mostrar los landmarks en el mapa
print("Landmarks en el mapa:", mapa.landmarks)





































