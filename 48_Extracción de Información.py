#Pablo Dario Jimenez Nu*o 21310143

import nltk
import re

# Oración de ejemplo
text = "John es un médico y Sarah es una abogada. Ambos son muy exitosos en sus carreras."

# Definir patrones de expresiones regulares para nombres y profesiones
name_pattern = re.compile(r'\b[A-Z][a-z]*\b')
profession_pattern = re.compile(r'\b(médico|abogado|ingeniero)\b')

# Encontrar nombres en el texto
names = name_pattern.findall(text)

# Encontrar profesiones en el texto
professions = profession_pattern.findall(text)

# Imprimir los resultados
print("Nombres encontrados:", names)
print("Profesiones encontradas:", professions)



























