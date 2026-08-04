"""
Exp-8.py: Stochastic Part-of-Speech Tagging
Implements a basic probabilistic (stochastic) model for POS tagging.
"""

from collections import defaultdict, Counter

class StochasticPOSTagger:
    def __init__(self):
        # Emission probabilities: P(word | tag)
        self.emission_counts = defaultdict(Counter)
        # Tag transition probabilities: P(tag_i | tag_{i-1})
        self.transition_counts = defaultdict(Counter)
        # Tag counts
        self.tag_counts = Counter()

    def train(self, tagged_corpus):
        for sentence in tagged_corpus:
            prev_tag = "START"
            for word, tag in sentence:
                word_lower = word.lower()
                self.emission_counts[tag][word_lower] += 1
                self.transition_counts[prev_tag][tag] += 1
                self.tag_counts[tag] += 1
                prev_tag = tag

    def tag(self, sentence_words):
        tagged_sentence = []
        prev_tag = "START"

        for word in sentence_words:
            w = word.lower()
            best_tag = None
            max_prob = -1.0

            # Find tag 't' maximizing P(t | prev_tag) * P(w | t)
            for tag, word_counts in self.emission_counts.items():
                # Emission prob
                p_emission = word_counts[w] / self.tag_counts[tag] if tag in self.tag_counts else 0.0
                
                # Transition prob
                trans_total = sum(self.transition_counts[prev_tag].values())
                p_transition = self.transition_counts[prev_tag][tag] / trans_total if trans_total > 0 else 0.0

                prob = p_transition * p_emission

                if prob > max_prob:
                    max_prob = prob
                    best_tag = tag

            # Fallback for unknown words (most frequent tag overall)
            if best_tag is None or max_prob == 0:
                best_tag = self.tag_counts.most_common(1)[0][0] if self.tag_counts else "NN"

            tagged_sentence.append((word, best_tag))
            prev_tag = best_tag

        return tagged_sentence

def demonstrate_stochastic_tagging():
    print("=== EXP-8: STOCHASTIC PART-OF-SPEECH TAGGING ===\n")

    # Sample Annotated Training Data
    training_data = [
        [("The", "DT"), ("dog", "NN"), ("barks", "VBZ"), ("loudly", "RB")],
        [("A", "DT"), ("cat", "NN"), ("meows", "VBZ"), ("softly", "RB")],
        [("The", "DT"), ("cat", "NN"), ("barks", "VBZ")],
        [("Dogs", "NNS"), ("and", "CC"), ("cats", "NNS"), ("run", "VBP")],
        [("The", "DT"), ("quick", "JJ"), ("fox", "NN"), ("jumps", "VBZ")]
    ]

    tagger = StochasticPOSTagger()
    tagger.train(training_data)

    test_sentence = ["The", "cat", "barks", "loudly"]
    result = tagger.tag(test_sentence)

    print("Training Corpus Sentences:", len(training_data))
    print("Test Sentence:", test_sentence)
    print("\nStochastic Tagging Output:")
    for word, tag in result:
        print(f"  {word:<10} -> {tag}")

if __name__ == "__main__":
    demonstrate_stochastic_tagging()
