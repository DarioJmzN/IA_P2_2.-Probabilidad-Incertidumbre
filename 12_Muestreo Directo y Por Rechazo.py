# Pablo Dario Jimenez Nu*o 21310143

import random

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

def muestreo_por_rechazo(distribucion, distribucion_propuesta, n):
    """
    Realiza muestreo por rechazo de una distribución discreta utilizando una distribución propuesta.

    Args:
    - distribucion (dict): Un diccionario donde las claves son los valores y los valores son las probabilidades de la
                           distribución objetivo.
    - distribucion_propuesta (dict): Un diccionario donde las claves son los valores y los valores son las probabilidades
                                     de la distribución propuesta.
    - n (int): El número de muestras a generar.

    Returns:
    - list: Una lista de muestras generadas por muestreo por rechazo.
    """
    muestras = []
    max_prob_propuesta = max(distribucion_propuesta.values())

    for _ in range(n):
        aceptado = False
        while not aceptado:
            muestra_propuesta = muestreo_directo(distribucion_propuesta)
            prob_aceptacion = distribucion[muestra_propuesta] / (max_prob_propuesta * distribucion_propuesta[muestra_propuesta])
            if random.random() < prob_aceptacion:
                muestras.append(muestra_propuesta)
                aceptado = True

    return muestras

# Ejemplo de uso
distribucion = {'a': 0.2, 'b': 0.3, 'c': 0.5}
distribucion_propuesta = {'a': 0.4, 'b': 0.3, 'c': 0.3}

# Muestreo directo
muestra_directo = muestreo_directo(distribucion)
print("Muestra utilizando muestreo directo:", muestra_directo)

# Muestreo por rechazo
muestras_por_rechazo = muestreo_por_rechazo(distribucion, distribucion_propuesta, 10)
print("Muestras utilizando muestreo por rechazo:", muestras_por_rechazo)














