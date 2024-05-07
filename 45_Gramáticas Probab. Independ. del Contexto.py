#Pablo Dario Jimenez Nu*o 21310143

import nltk
from nltk import PCFG

# Definir la PCFG
grammar = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.5] | N [0.5]
    VP -> V [0.7] | V NP [0.3]
    Det -> 'the' [0.6] | 'a' [0.4]
    N -> 'dog' [0.5] | 'cat' [0.5]
    V -> 'chased' [0.3] | 'sat' [0.7]
""")

# Generar oraciones a partir de la gramática
parser = nltk.ViterbiParser(grammar)
for tree in parser.parse(['the', 'dog', 'chased']):
    print(tree)
























