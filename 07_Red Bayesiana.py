# Pablo Dario Jimenez Nu*o 21310143

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

# Definimos la estructura de la red bayesiana
modelo = BayesianNetwork([('D', 'G'), ('I', 'G'), ('G', 'L'), ('I', 'S')])

# Definimos las distribuciones de probabilidad condicional (CPD)
cpd_d = TabularCPD(variable='D', variable_card=2, values=[[0.6], [0.4]])
cpd_i = TabularCPD(variable='I', variable_card=2, values=[[0.7], [0.3]])
cpd_g = TabularCPD(variable='G', variable_card=3, 
                   values=[[0.3, 0.4, 0.3, 0.9, 0.6, 0.01],
                           [0.4, 0.3, 0.4, 0.08, 0.3, 0.01],
                           [0.3, 0.3, 0.3, 0.02, 0.1, 0.98]],
                   evidence=['I', 'D'], evidence_card=[2, 2])
cpd_l = TabularCPD(variable='L', variable_card=2, 
                   values=[[0.1, 0.4, 0.99], [0.9, 0.6, 0.01]],
                   evidence=['G'], evidence_card=[3])
cpd_s = TabularCPD(variable='S', variable_card=2, 
                   values=[[0.95, 0.2], [0.05, 0.8]],
                   evidence=['I'], evidence_card=[2])

# Añadimos las CPD al modelo
modelo.add_cpds(cpd_d, cpd_i, cpd_g, cpd_l, cpd_s)

# Verificamos si el modelo es válido
print("¿Es el modelo válido?", modelo.check_model())

# Imprimimos las CPD del modelo
print("\nCPDs del modelo:")
for cpd in modelo.get_cpds():
    print(cpd)

# Calculamos la probabilidad conjunta de las variables D y G
print("\nProbabilidad conjunta de D y G:")
print(modelo.get_independencies())

# Obtenemos las variables que dependen de G
print("\nVariables que dependen de G:")
print(modelo.active_trail_nodes('G'))

# Obtenemos el razonamiento causal de la variable G
print("\nRazonamiento causal de G:")
print(modelo.active_trail_nodes('G', observed='D'))












