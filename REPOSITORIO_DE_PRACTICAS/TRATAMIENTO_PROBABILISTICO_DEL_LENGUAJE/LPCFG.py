import nltk
from nltk.grammar import Nonterminal, CFG
from nltk.parse.chart import ChartParser

# Define una gramática regular (CFG) sin probabilidades
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'el' | 'un'
    N -> 'perro' | 'gato' | 'ratón'
    V -> 'persigue' | 'captura'
""")

# Crear un parser para la gramática regular
parser = ChartParser(grammar)

# Generar oraciones basadas en la gramática
for tree in parser.parse("el perro persigue el gato".split()):
    print(tree)
