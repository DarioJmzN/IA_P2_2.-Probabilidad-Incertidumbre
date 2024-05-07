# Pablo Dario Jimenez Nu*o 21310143

def probabilidad_condicionada(evento_A, evento_B, espacio_muestral):
    """
    Calcula la probabilidad condicionada de evento_A dado evento_B en el espacio muestral.

    Args:
    - evento_A (str): El evento cuya probabilidad condicionada queremos calcular.
    - evento_B (str): El evento que ya ha ocurrido.
    - espacio_muestral (list): La lista de todos los posibles resultados en el espacio muestral.

    Returns:
    - float: La probabilidad condicionada de evento_A dado evento_B.
    """
    num_ocurrencias_B = espacio_muestral.count(evento_B)
    num_ocurrencias_A_y_B = espacio_muestral.count(evento_A) if evento_A in espacio_muestral else 0
    if num_ocurrencias_B == 0:
        return 0
    return num_ocurrencias_A_y_B / num_ocurrencias_B

def normalizar_probabilidades(probabilidades):
    """
    Normaliza una lista de probabilidades para que sumen 1.

    Args:
    - probabilidades (list): La lista de probabilidades a normalizar.

    Returns:
    - list: La lista de probabilidades normalizadas.
    """
    suma_total = sum(probabilidades)
    return [p / suma_total for p in probabilidades]

# Definimos el espacio muestral
espacio_muestral = ['soleado', 'lluvioso', 'nublado', 'soleado', 'nublado', 'lluvioso']

# Calculamos la probabilidad condicionada de que sea soleado dado que ya es lluvioso
probabilidad_condicionada_soleado = probabilidad_condicionada('soleado', 'lluvioso', espacio_muestral)
print("La probabilidad condicionada de que sea soleado dado que es lluvioso es:", probabilidad_condicionada_soleado)

# Normalizamos las probabilidades
probabilidades = [0.3, 0.2, 0.5]
probabilidades_normalizadas = normalizar_probabilidades(probabilidades)
print("Probabilidades normalizadas:", probabilidades_normalizadas)
print("Suma de las probabilidades normalizadas:", sum(probabilidades_normalizadas))










