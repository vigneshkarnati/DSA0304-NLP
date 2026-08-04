import random

text = "I love natural language processing because natural language is interesting"

words = text.split()

bigram = {}

for i in range(len(words) - 1):
    current = words[i]
    next_word = words[i + 1]

    if current not in bigram:
        bigram[current] = []

    bigram[current].append(next_word)

start = "natural"
result = [start]

for i in range(10):
    if start in bigram:
        next_word = random.choice(bigram[start])
        result.append(next_word)
        start = next_word
    else:
        break

print("Generated Text:")
print(" ".join(result))