import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('wordnet')

ps = PorterStemmer()
lm = WordNetLemmatizer()

word = input("Enter a word: ")

print("Original Word:", word)
print("Stemmed Word:", ps.stem(word))
print("Lemmatized Word:", lm.lemmatize(word))