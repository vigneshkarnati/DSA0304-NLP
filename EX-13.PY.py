import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'cat' | 'dog'
V -> 'sees' | 'likes'
""")

sentence = "the cat sees the dog".split()

parser = nltk.ChartParser(grammar)

print("Parse Tree:")

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()