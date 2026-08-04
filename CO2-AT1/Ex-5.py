from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "running", "studies", "cats", "jumped"]

print("Original Words\tStemmed Words")

for word in words:
    print(word, "\t\t", ps.stem(word))