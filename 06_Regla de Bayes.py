# Pablo Dario Jimenez Nu*o 21310143

def regla_de_bayes(probabilidad_A, probabilidad_B_dado_A, probabilidad_B):
    """
    Calcula la probabilidad condicional de A dado B utilizando la Regla de Bayes.

    Args:
    - probabilidad_A (float): La probabilidad a priori de A.
    - probabilidad_B_dado_A (float): La probabilidad de B dado A.
    - probabilidad_B (float): La probabilidad marginal de B.

    Returns:
    - float: La probabilidad condicional de A dado B.
    """
    return (probabilidad_B_dado_A * probabilidad_A) / probabilidad_B

# Ejemplo de la Regla de Bayes
probabilidad_A = 0.3  # Probabilidad a priori de A
probabilidad_B_dado_A = 0.8  # Probabilidad de B dado A
probabilidad_B = 0.5  # Probabilidad marginal de B

# Calculamos la probabilidad condicional de A dado B utilizando la Regla de Bayes
probabilidad_A_dado_B = regla_de_bayes(probabilidad_A, probabilidad_B_dado_A, probabilidad_B)

# Imprimimos el resultado
print("La probabilidad condicional de A dado B es:", probabilidad_A_dado_B)











