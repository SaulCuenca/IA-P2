import nltk
from nltk.grammar import Nonterminal, CFG
from nltk.parse.chart import ChartParser

# Define una gram�tica regular (CFG) sin probabilidades
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'el' | 'un'
    N -> 'perro' | 'gato' | 'rat�n'
    V -> 'persigue' | 'captura'
""")

# Crear un parser para la gram�tica regular
parser = ChartParser(grammar)

# Generar oraciones basadas en la gram�tica
for tree in parser.parse("el perro persigue el gato".split()):
    print(tree)
