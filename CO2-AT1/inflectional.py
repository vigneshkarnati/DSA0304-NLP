import re

class MorphologicalAnalyzer:
    def __init__(self):
        # Define suffix rules: (suffix, type, description)
        self.rules = [
            ('ed', 'Inflectional', 'past tense'),
            ('ing', 'Inflectional', 'present participle'),
            ('ion', 'Derivational', 'noun formation'),
            # Additional suffixes can be added here
        ]
        # Sort suffixes by length descending to handle overlapping cases
        self.rules.sort(key=lambda x: len(x[0]), reverse=True)

    def analyze(self, word):
        word_lower = word.lower()
        for suffix, suffix_type, description in self.rules:
            if word_lower.endswith(suffix):
                root = word_lower[:-len(suffix)]
                # Avoid empty root (e.g., if word is just suffix)
                if root:
                    return {
                        'word': word,
                        'root': root,
                        'suffix': suffix,
                        'type': suffix_type,
                        'description': description,
                        'normalized': root
                    }
        # If no rule matches, treat the whole word as root
        return {
            'word': word,
            'root': word,
            'suffix': '',
            'type': 'None',
            'description': 'No suffix',
            'normalized': word
        }

    def analyze_words(self, words):
        results = []
        for w in words:
            results.append(self.analyze(w))
        return results

    def display_table(self, results):
        # Print a formatted table
        header = f"{'Word':<12} {'Root':<10} {'Suffix':<8} {'Type':<14} {'Normalized':<12}"
        print(header)
        print('-' * len(header))
        for r in results:
            print(f"{r['word']:<12} {r['root']:<10} {r['suffix']:<8} {r['type']:<14} {r['normalized']:<12}")

def main():
    words = ["connected", "connecting", "connection"]
    analyzer = MorphologicalAnalyzer()
    results = analyzer.analyze_words(words)
    analyzer.display_table(results)

if __name__ == "__main__":
    main()