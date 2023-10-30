import nltk
from nltk.grammar import Nonterminal, Production

# Define una gram�tica probabil�stica
producciones = [
    # S -> NP VP
    Production(Nonterminal('S'), [Nonterminal('NP'), Nonterminal('VP')]),
    # NP -> Det N
    Production(Nonterminal('NP'), [Nonterminal('Det'), Nonterminal('N')]),
    # NP -> N
    Production(Nonterminal('NP'), [Nonterminal('N')]),
    # VP -> V NP
    Production(Nonterminal('VP'), [Nonterminal('V'), Nonterminal('NP')]),
    # VP -> V
    Production(Nonterminal('VP'), [Nonterminal('V')]),
    # Det -> 'el'
    Production(Nonterminal('Det'), ['el']),
    # Det -> 'un'
    Production(Nonterminal('Det'), ['un']),
    # N -> 'perro'
    Production(Nonterminal('N'), ['perro']),
    # N -> 'gato'
    Production(Nonterminal('N'), ['gato']),
    # N -> 'rat�n'
    Production(Nonterminal('N'), ['rat�n']),
    # V -> 'persigue'
    Production(Nonterminal('V'), ['persigue']),
    # V -> 'captura'
    Production(Nonterminal('V'), ['captura'])
]

# Crear una gram�tica probabil�stica
pcfg = nltk.grammar.induce_pcfg(Nonterminal('S'), producciones)

# Crear un parser para la gram�tica probabil�stica
parser = nltk.ViterbiParser(pcfg)

# Generar oraciones basadas en la gram�tica
for tree in parser.parse("el perro persigue el gato".split()):
    print(tree)
