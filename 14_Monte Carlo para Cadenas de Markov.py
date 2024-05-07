# Pablo Dario Jimenez Nu*o 21310143

import random

def monte_carlo_cadenas_markov(matriz_transicion, estado_inicial, n):
    """
    Realiza el algoritmo de Monte Carlo para Cadenas de Markov.

    Args:
    - matriz_transicion (dict): Un diccionario que representa la matriz de transición de la cadena de Markov.
                                 Las claves son los estados y los valores son diccionarios donde las claves son los
                                 estados alcanzables desde el estado actual y los valores son las probabilidades de
                                 transición a esos estados.
    - estado_inicial (any): El estado inicial de la cadena de Markov.
    - n (int): El número de pasos en la cadena de Markov.

    Returns:
    - list: Una lista de estados visitados en la cadena de Markov.
    """
    estados_visitados = [estado_inicial]

    estado_actual = estado_inicial
    for _ in range(n):
        proximo_estado = muestreo_directo(matriz_transicion[estado_actual])
        estados_visitados.append(proximo_estado)
        estado_actual = proximo_estado

    return estados_visitados

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
matriz_transicion = {
    'A': {'A': 0.4, 'B': 0.6},
    'B': {'A': 0.3, 'B': 0.7}
}
estado_inicial = 'A'
n = 10

estados_visitados = monte_carlo_cadenas_markov(matriz_transicion, estado_inicial, n)
print("Estados visitados en la cadena de Markov:", estados_visitados)















