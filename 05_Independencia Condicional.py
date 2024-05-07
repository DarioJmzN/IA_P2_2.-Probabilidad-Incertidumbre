# Pablo Dario Jimenez Nu*o 21310143

def independencia_condicional(evento_A, evento_B, evento_C, espacio_muestral):
    """
    Comprueba si los eventos A y B son independientes dado el evento C en el espacio muestral dado.

    Args:
    - evento_A (str): El primer evento.
    - evento_B (str): El segundo evento.
    - evento_C (str): El evento condicionante.
    - espacio_muestral (list): La lista de todos los posibles resultados en el espacio muestral.

    Returns:
    - bool: True si A y B son independientes dado C, False de lo contrario.
    """
    # Calcula las probabilidades condicionadas
    prob_A_dado_C = probabilidad_condicionada(evento_A, evento_C, espacio_muestral)
    prob_B_dado_C = probabilidad_condicionada(evento_B, evento_C, espacio_muestral)

    # Si los eventos A y B son independientes dado C, entonces P(A|C) = P(A) y P(B|C) = P(B)
    return np.isclose(prob_A_dado_C, probabilidad_a_priori(evento_A, espacio_muestral)) and \
           np.isclose(prob_B_dado_C, probabilidad_a_priori(evento_B, espacio_muestral))

# Ejemplo de espacio muestral
espacio_muestral = ['soleado', 'lluvioso', 'nublado', 'soleado', 'nublado', 'lluvioso']

# Definimos los eventos A, B y C
evento_A = 'soleado'
evento_B = 'nublado'
evento_C = 'lluvioso'

# Comprobamos la independencia condicional de A y B dado C
es_independiente_condicionalmente = independencia_condicional(evento_A, evento_B, evento_C, espacio_muestral)
if es_independiente_condicionalmente:
    print("Los eventos A y B son independientes dado C.")
else:
    print("Los eventos A y B no son independientes dado C.")


# Imprimimos los resultados
print("Valores:", valores)
print("Probabilidades:", probabilidades)
print("Media:", media)
print("Varianza:", varianza)


# Normalizamos las probabilidades
probabilidades = [0.3, 0.2, 0.5]
probabilidades_normalizadas = normalizar_probabilidades(probabilidades)
print("Probabilidades normalizadas:", probabilidades_normalizadas)
print("Suma de las probabilidades normalizadas:", sum(probabilidades_normalizadas))










