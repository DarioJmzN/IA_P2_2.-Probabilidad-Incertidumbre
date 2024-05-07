# Pablo Dario Jimenez Nu*o 21310143

def regla_de_la_cadena(evento_A, evento_B_dado_A, evento_C_dado_B):
    """
    Calcula la probabilidad conjunta de A, B y C utilizando la regla de la cadena.

    Args:
    - evento_A (float): La probabilidad del evento A.
    - evento_B_dado_A (float): La probabilidad del evento B dado A.
    - evento_C_dado_B (float): La probabilidad del evento C dado B.

    Returns:
    - float: La probabilidad conjunta de A, B y C.
    """
    return evento_A * evento_B_dado_A * evento_C_dado_B

# Ejemplo de la regla de la cadena
evento_A = 0.3  # Probabilidad del evento A
evento_B_dado_A = 0.7  # Probabilidad del evento B dado A
evento_C_dado_B = 0.5  # Probabilidad del evento C dado B

# Calculamos la probabilidad conjunta de A, B y C utilizando la regla de la cadena
probabilidad_conjunta = regla_de_la_cadena(evento_A, evento_B_dado_A, evento_C_dado_B)

# Imprimimos el resultado
print("La probabilidad conjunta de A, B y C es:", probabilidad_conjunta)












