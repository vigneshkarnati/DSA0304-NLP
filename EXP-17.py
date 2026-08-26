from nltk.corpus import wordnet

word = "bank"

synsets = wordnet.synsets(word)

print("Word:", word)
print("Number of Synsets:", len(synsets))

for synset in synsets[:5]:
    print("\nSynset:", synset.name())
    print("Definition:", synset.definition())
    print("Examples:", synset.examples())

    synonyms = []

    for lemma in synset.lemmas():
        synonyms.append(lemma.name())

    print("Synonyms:", synonyms)