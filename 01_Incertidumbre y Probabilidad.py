# Pablo Dario Jimenez Nu*o 21310143

import numpy as np

# Generar un conjunto de datos de ejemplo
datos = np.random.binomial(n=1, p=0.5, size=1000)

# Calcular la probabilidad de obtener 1 (éxito)
probabilidad_exito = np.mean(datos)
print("La probabilidad de obtener 1 (éxito) es:", probabilidad_exito)

# Calcular la probabilidad de obtener 0 (fracaso)
probabilidad_fracaso = 1 - probabilidad_exito
print("La probabilidad de obtener 0 (fracaso) es:", probabilidad_fracaso)

# Calcular la media y la varianza de los datos generados
media = np.mean(datos)
varianza = np.var(datos)
print("La media de los datos es:", media)
print("La varianza de los datos es:", varianza)

# Generar muestras de una distribución normal (Gaussiana)
muestras = np.random.normal(loc=media, scale=np.sqrt(varianza), size=1000)

# Calcular la media y la varianza de las muestras generadas
media_muestras = np.mean(muestras)
varianza_muestras = np.var(muestras)
print("La media de las muestras generadas es:", media_muestras)
print("La varianza de las muestras generadas es:", varianza_muestras)




