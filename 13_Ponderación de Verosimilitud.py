# Pablo Dario Jimenez Nu*o 21310143

import random

def ponderacion_verosimilitud(distribucion, n):
    """
    Realiza el algoritmo de Ponderación de Verosimilitud para una distribución discreta.

    Args:
    - distribucion (dict): Un diccionario donde las claves son los valores y los valores son las probabilidades de la
                           distribución objetivo.
    - n (int): El número de muestras a generar.

    Returns:
    - list: Una lista de muestras generadas por Ponderación de Verosimilitud.
    - list: Una lista de pesos asociados a las muestras generadas.
    """
    muestras = []
    pesos = []

    for _ in range(n):
        muestra = muestreo_directo(distribucion)
        peso = distribucion[muestra]
        muestras.append(muestra)
        pesos.append(peso)

    return muestras, pesos

def muestreo_directo(distribucion):
    """
    Realiza muestreo directo de una distribución discreta.

    Args:
    - distribucion (dict): Un diccionario donde las claves son los valores y los valores son las probabilidades.

    Returns:
    - any: Una muestra aleatoria de la distribución.
    """
    valor = random.random()
    suma_probabilidad = 0
    for k, v in distribucion.items():
        suma_probabilidad += v
        if valor < suma_probabilidad:
            return k

# Ejemplo de uso
distribucion = {'a': 0.2, 'b': 0.3, 'c': 0.5}
n = 10

muestras, pesos = ponderacion_verosimilitud(distribucion, n)
print("Muestras generadas:", muestras)
print("Pesos asociados a las muestras:", pesos)














