import nltk

grammar = nltk.PCFG.fromstring("""
S -> NP VP [1.0]

NP -> Det N [0.6]
NP -> Det Adj N [0.4]

VP -> V NP [1.0]

Det -> 'the' [1.0]

Adj -> 'big' [1.0]

N -> 'dog' [0.5]
N -> 'cat' [0.5]

V -> 'sees' [0.5]
V -> 'likes' [0.5]
""")

sentence = "the big dog sees the cat".split()

parser = nltk.ViterbiParser(grammar)

print("Most Probable Parse:")

for tree in parser.parse(sentence):
    print(tree)
    print("Probability:", tree.prob())
    tree.pretty_print()