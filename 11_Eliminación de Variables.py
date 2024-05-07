# Pablo Dario Jimenez Nu*o 21310143

class RedBayesiana:
    def __init__(self, nodos, probabilidad_condicional):
        """
        Inicializa la red bayesiana.

        Args:
        - nodos (dict): Un diccionario donde las claves son los nombres de los nodos y los valores son las posibles
                        observaciones de cada nodo.
        - probabilidad_condicional (dict): Un diccionario donde las claves son los nombres de los nodos y los valores
                                           son las tablas de probabilidad condicional para cada nodo.
        """
        self.nodos = nodos
        self.probabilidad_condicional = probabilidad_condicional

    def inferencia_elim_vars(self, variable, evidencia):
        """
        Calcula la probabilidad de la variable dado un conjunto de evidencia utilizando Eliminación de Variables.

        Args:
        - variable (str): El nombre de la variable de interés.
        - evidencia (dict): Un diccionario donde las claves son los nombres de los nodos y los valores son las
                            observaciones de cada nodo en la evidencia.

        Returns:
        - float: La probabilidad de la variable dado la evidencia.
        """
        variables_ocultas = set(self.nodos.keys()) - set(evidencia.keys()) - {variable}
        suma_sobre = {}
        for oculta in variables_ocultas:
            suma_sobre[oculta] = sum(self.calcular_marginal(oculta, evidencia))

        # Calculamos la probabilidad conjunta de la evidencia
        prob_conjunta_evidencia = 1.0
        for nodo, observacion in evidencia.items():
            prob_conjunta_evidencia *= self.probabilidad_condicional[nodo][observacion]

        # Calculamos la probabilidad de la variable de interés sumando sobre las variables ocultas
        probabilidad_variable = 0.0
        for observacion in self.nodos[variable]:
            nueva_evidencia = evidencia.copy()
            nueva_evidencia[variable] = observacion
            prob_conjunta = prob_conjunta_evidencia
            for oculta, suma in suma_sobre.items():
                prob_conjunta *= suma
            probabilidad_variable += prob_conjunta
        return probabilidad_variable

    def calcular_marginal(self, variable, evidencia):
        """
        Calcula la marginal de la variable dada la evidencia.

        Args:
        - variable (str): El nombre de la variable de interés.
        - evidencia (dict): Un diccionario donde las claves son los nombres de los nodos y los valores son las
                            observaciones de cada nodo en la evidencia.

        Returns:
        - list: La marginal de la variable dada la evidencia.
        """
        prob_marginal = []
        for observacion in self.nodos[variable]:
            nueva_evidencia = evidencia.copy()
            nueva_evidencia[variable] = observacion
            prob_marginal.append(self.probabilidad_conjunta(nueva_evidencia))
        return prob_marginal

    def probabilidad_conjunta(self, evidencia):
        """
        Calcula la probabilidad conjunta de la red bayesiana dados la evidencia.

        Args:
        - evidencia (dict): Un diccionario donde las claves son los nombres de los nodos y los valores son las
                            observaciones de cada nodo en la evidencia.

        Returns:
        - float: La probabilidad conjunta de la red bayesiana.
        """
        probabilidad_conjunta = 1.0
        for nodo, observacion in evidencia.items():
            probabilidad_conjunta *= self.probabilidad_condicional[nodo][observacion]
        return probabilidad_conjunta


# Ejemplo de una red bayesiana
nodos = {
    'A': ['A1', 'A2'],
    'B': ['B1', 'B2'],
    'C': ['C1', 'C2']
}

probabilidad_condicional = {
    'A': {'A1': 0.3, 'A2': 0.7},
    'B': {'B1': 0.4, 'B2': 0.6},
    'C': {'C1': 0.5, 'C2': 0.5}
}

red_bayesiana = RedBayesiana(nodos, probabilidad_condicional)

# Calculamos la probabilidad de la variable C dado que A= A1 y B= B1
evidencia = {'A': 'A1', 'B': 'B1'}
probabilidad = red_bayesiana.inferencia_elim_vars('C', evidencia)
print("La probabilidad de C dado A=A1 y B=B1 es:", probabilidad)













