# Pablo Dario Jimenez Nu*o 21310143

def probabilidad_a_priori(evento, espacio_muestral):
    """
    Calcula la probabilidad a priori de un evento en un espacio muestral.

    Args:
    - evento (str): El evento del cual se quiere calcular la probabilidad a priori.
    - espacio_muestral (list): La lista de todos los posibles resultados en el espacio muestral.

    Returns:
    - float: La probabilidad a priori del evento.
    """
    num_ocurrencias_evento = espacio_muestral.count(evento)
    total_eventos = len(espacio_muestral)
    return num_ocurrencias_evento / total_eventos

# Definimos el espacio muestral de lanzar un dado
dado = [1, 2, 3, 4, 5, 6]

# Calculamos la probabilidad a priori de obtener un 3 al lanzar el dado
probabilidad_tres = probabilidad_a_priori(3, dado)
print("La probabilidad a priori de obtener un 3 es:", probabilidad_tres)









