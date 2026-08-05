class SearchEngineStemmer:
    def __init__(self):
        # Define suffix rules: (suffix, type, description)
        # Sorted by length descending to ensure 'ing' is checked before 'ed'
        self.rules = [
            ('ing', 'Inflectional', 'present participle / gerund'),
            ('ed', 'Inflectional', 'past tense'),
            ('er', 'Derivational', 'agent noun formation'),
        ]
        self.rules.sort(key=lambda x: len(x[0]), reverse=True)

    def stem_word(self, word):
        """
        Process a single word: strip the longest matching suffix,
        classify it, and return the structured result.
        """
        word_lower = word.lower()

        # 1. Try to strip a suffix
        for suffix, typ, desc in self.rules:
            if word_lower.endswith(suffix):
                stem = word_lower[:-len(suffix)]
                # Ensure we don't end up with an empty stem
                if stem:
                    return {
                        'original': word,
                        'stem': stem,
                        'affix': suffix,
                        'type': typ,
                        'description': desc,
                        'normalized': stem
                    }

        # 2. Fallback: no suffix matched
        return {
            'original': word,
            'stem': word_lower,
            'affix': '',
            'type': 'None',
            'description': 'No removable suffix found',
            'normalized': word_lower
        }

    def process_words(self, words):
        """Process a list of words and return a list of results."""
        return [self.stem_word(w) for w in words]

    def display_table(self, results):
        """Display the morphological breakdown in a clean tabular format."""
        # Define column headers
        headers = ['Original', 'Stem', 'Affix', 'Type', 'Description', 'Normalized']
        col_widths = [12, 10, 8, 14, 30, 12]
        
        # Print header
        header_line = '  '.join(f'{h:<{w}}' for h, w in zip(headers, col_widths))
        print(header_line)
        print('-' * len(header_line))

        # Print each row
        for r in results:
            row = [
                r['original'],
                r['stem'],
                r['affix'] if r['affix'] else '—',
                r['type'],
                r['description'],
                r['normalized']
            ]
            line = '  '.join(f'{str(val):<{w}}' for val, w in zip(row, col_widths))
            print(line)


def main():
    # Input words
    input_words = ["played", "player", "playing"]
    
    # Instantiate the stemmer and process the words
    stemmer = SearchEngineStemmer()
    results = stemmer.process_words(input_words)
    
    # Display the output
    stemmer.display_table(results)


if __name__ == "__main__":
    main()