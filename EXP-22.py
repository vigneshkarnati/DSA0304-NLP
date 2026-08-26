import re

text = "Ravi went to the library. He borrowed a book. The book was interesting. He read it."

pronouns = ["he", "she", "it", "they"]

# Find simple nouns/proper names
words = re.findall(r"\b[A-Za-z]+\b", text)

references = []

for i, word in enumerate(words):
    if word.lower() in pronouns:
        previous_nouns = []

        for previous in words[:i]:
            if previous.lower() not in pronouns:
                previous_nouns.append(previous)

        if previous_nouns:
            reference = previous_nouns[-1]
            references.append((word, reference))

print("Reference Resolution:")

for pronoun, reference in references:
    print(pronoun, "->", reference)