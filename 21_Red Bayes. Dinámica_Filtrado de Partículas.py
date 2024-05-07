#Pablo Dario Jimenez Nu*o 21310143

import numpy as np

class ParticleFilter:
    def __init__(self, num_particles, motion_noise, measurement_noise):
        """
        Inicializa el filtro de partículas.

        Args:
            num_particles (int): Número de partículas.
            motion_noise (float): Varianza del ruido del movimiento.
            measurement_noise (float): Varianza del ruido de la medición.
        """
        self.num_particles = num_particles
        self.motion_noise = motion_noise
        self.measurement_noise = measurement_noise
        self.particles = None

    def initialize_particles(self, initial_state):
        """
        Inicializa las partículas con un estado inicial.

        Args:
            initial_state (numpy.ndarray): Estado inicial.
        """
        self.particles = np.random.normal(initial_state, self.motion_noise, size=(self.num_particles, len(initial_state)))

    def predict(self, control_input):
        """
        Predice el siguiente estado de las partículas basado en el modelo de movimiento.

        Args:
            control_input (numpy.ndarray): Entrada de control/movimiento.
        """
        self.particles += np.random.normal(0, self.motion_noise, size=self.particles.shape)
        self.particles += control_input

    def update(self, measurement):
        """
        Actualiza las ponderaciones de las partículas basado en la medición.

        Args:
            measurement (numpy.ndarray): Medición observada.
        """
        weights = np.exp(-0.5 * np.sum((self.particles - measurement)**2 / self.measurement_noise**2, axis=1))
        weights /= np.sum(weights)
        self.particles = np.random.choice(self.particles, size=self.num_particles, p=weights)

    def get_estimated_state(self):
        """
        Obtiene la estimación del estado basada en las partículas.

        Returns:
            numpy.ndarray: Estado estimado.
        """
        return np.mean(self.particles, axis=0)

# Ejemplo de uso
num_particles = 100
motion_noise = 0.1
measurement_noise = 0.1

# Crear filtro de partículas
particle_filter = ParticleFilter(num_particles, motion_noise, measurement_noise)

# Inicializar las partículas con un estado inicial
initial_state = np.array([0, 0])
particle_filter.initialize_particles(initial_state)

# Secuencia de mediciones
measurements = np.array([[1, 1], [2, 2], [3, 3]])

# Aplicar el filtro de partículas
for measurement in measurements:
    # Predicción
    control_input = np.array([1, 1])  # Entrada de control/movimiento
    particle_filter.predict(control_input)

    # Actualización
    particle_filter.update(measurement)

    # Obtener la estimación del estado
    estimated_state = particle_filter.get_estimated_state()
    print("Estado estimado después de la medición {}: {}".format(measurement, estimated_state))


