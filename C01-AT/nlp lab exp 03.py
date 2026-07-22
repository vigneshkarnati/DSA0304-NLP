import nltk
from nltk.stem import PorterStemmer

# Create a Porter Stemmer object
ps = PorterStemmer()

# Get input from the user
text = input("Enter words separated by spaces: ")

# Split the sentence into words
words = text.split()

print("\nMorphological Analysis")
print("----------------------")

# Find the stem of each word
for word in words:
    stem = ps.stem(word)
    print("Word :", word)
    print("Stem :", stem)
    print()