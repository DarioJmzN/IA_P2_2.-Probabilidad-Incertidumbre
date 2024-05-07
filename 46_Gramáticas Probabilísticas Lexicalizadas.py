#Pablo Dario Jimenez Nu*o 21310143

import nltk
from nltk import PCFG
from nltk.grammar import CFG, Nonterminal, Production

# Definir la gramática probabilística lexicalizada
grammar = PCFG.fromstring("""
    S -> NP VP [0.9]
    VP -> V NP [0.5] | V [0.5]
    NP -> Det N [0.6] | N [0.4]
    V -> 'saw' [0.3] | 'ate' [0.7]
    Det -> 'the' [0.5] | 'a' [0.5]
    N -> 'dog' [0.4] | 'cat' [0.6]
""")

# Convertir la gramática en una gramática de contexto libre (CFG)
cfg_grammar = CFG.fromstring(str(grammar))

# Generar oraciones a partir de la gramática
parser = nltk.ChartParser(cfg_grammar)
for tree in parser.parse(['the', 'dog', 'ate']):
    print(tree)

























