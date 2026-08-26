import re

sentence = "The intelligent student reads a book in the library."

# Extract simple noun phrases
pattern = r"\b(?:the|a|an)\s+(?:\w+\s+)?\w+\b"

noun_phrases = re.findall(pattern, sentence, re.IGNORECASE)

print("Sentence:", sentence)
print("\nNoun Phrases and Meanings:")

for phrase in noun_phrases:
    words = phrase.lower().split()
    noun = words[-1]

    if noun in ["student", "teacher", "person"]:
        meaning = "Person"
    elif noun in ["book", "computer", "phone"]:
        meaning = "Object"
    elif noun in ["library", "school", "college"]:
        meaning = "Place"
    else:
        meaning = "Entity"

    print(phrase, "->", meaning)