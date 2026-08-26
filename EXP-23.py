import math
import re

text = """
Python is a programming language.
Python is widely used for machine learning.
Machine learning is used in many applications.
Applications can solve real world problems.
"""

sentences = [
    s.strip()
    for s in re.split(r"[.!?]", text)
    if s.strip()
]

def vector(sentence):
    words = re.findall(r"\b[a-z]+\b", sentence.lower())
    return set(words)

def similarity(a, b):
    common = len(a & b)
    total = len(a | b)

    if total == 0:
        return 0

    return common / total

scores = []

for i in range(len(sentences) - 1):
    score = similarity(
        vector(sentences[i]),
        vector(sentences[i + 1])
    )
    scores.append(score)

average = sum(scores) / len(scores)

print("Coherence Scores:")
for i, score in enumerate(scores):
    print(
        "Sentence", i + 1,
        "and Sentence", i + 2,
        ":", round(score, 2)
    )

print("\nAverage Coherence:", round(average, 2))

if average >= 0.10:
    print("Text is reasonably coherent.")
else:
    print("Text has low coherence.")