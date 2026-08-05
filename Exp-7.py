"""
Exp-7.py: POS Tagging using NLTK
Performs part-of-speech tagging on a sample sentence using NLTK.
"""

from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

# POS Tag Explanation Mapping
POS_DESCRIPTIONS = {
    'NN': 'Noun, singular',
    'NNS': 'Noun, plural',
    'NNP': 'Proper noun, singular',
    'VB': 'Verb, base form',
    'VBD': 'Verb, past tense',
    'VBG': 'Verb, gerund or present participle',
    'VBN': 'Verb, past participle',
    'VBP': 'Verb, non-3rd person singular present',
    'VBZ': 'Verb, 3rd person singular present',
    'JJ': 'Adjective',
    'RB': 'Adverb',
    'IN': 'Preposition or subordinating conjunction',
    'DT': 'Determiner',
    'PRP': 'Personal pronoun',
    'PRP$': 'Possessive pronoun'
}

def demonstrate_pos_tagging():
    print("=== EXP-7: NLTK PART-OF-SPEECH (POS) TAGGING ===\n")
    
    text = "The quick brown fox jumps over the lazy dog near the river."
    print("Input Text:", text)

    tokens = word_tokenize(text)
    tagged_words = pos_tag(tokens)

    print("\nPOS Tagged Tokens:")
    print(f"{'Word':<15} | {'POS Tag':<10} | {'Description':<35}")
    print("-" * 65)

    for word, tag in tagged_words:
        desc = POS_DESCRIPTIONS.get(tag, 'Other Grammar Symbol')
        print(f"{word:<15} | {tag:<10} | {desc:<35}")

if __name__ == "__main__":
    demonstrate_pos_tagging()
