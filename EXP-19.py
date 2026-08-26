from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

sentence = "I went to the bank to deposit money."

words = word_tokenize(sentence)

sense = lesk(words, "bank")

if sense:
    print("Word: bank")
    print("Selected Synset:", sense.name())
    print("Definition:", sense.definition())
else:
    print("No sense found")