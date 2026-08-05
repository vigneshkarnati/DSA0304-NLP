import re

class SentimentMorphParser:
    def __init__(self):
        # Prefix rules: (prefix, type, description)
        self.prefixes = [
            ('un', 'Derivational', 'negation'),
        ]
        # Suffix rules: (suffix, type, transform_function, description)
        # transform_function converts the stripped stem back to the root
        self.suffixes = [
            ('ness', 'Derivational', self._restore_y, 'noun formation'),
            ('ly',   'Derivational', self._restore_y, 'adverb formation'),
        ]
        # Sort suffixes by length descending to avoid false matches
        self.suffixes.sort(key=lambda x: len(x[0]), reverse=True)

    def _restore_y(self, stem):
        """If stem ends with 'i', change it back to 'y' (e.g., happi -> happy)."""
        if stem.endswith('i'):
            return stem[:-1] + 'y'
        return stem

    def parse(self, word):
        word_lower = word.lower()
        parsed = {
            'word': word,
            'prefix': '',
            'root': '',
            'suffix': '',
            'type': 'None',
            'description': '',
            'normalized': ''
        }

        # 1. Try to strip a suffix (longest match first)
        for suffix, typ, transform, desc in self.suffixes:
            if word_lower.endswith(suffix):
                stem = word_lower[:-len(suffix)]
                if stem:  # root must not be empty
                    root = transform(stem)
                    parsed['suffix'] = suffix
                    parsed['root'] = root
                    parsed['type'] = typ
                    parsed['description'] = desc
                    parsed['normalized'] = root
                    break

        # 2. If no suffix was found, try to strip a prefix
        if not parsed['root']:
            for prefix, typ, desc in self.prefixes:
                if word_lower.startswith(prefix):
                    remainder = word_lower[len(prefix):]
                    if remainder:  # must leave a non‑empty root
                        parsed['prefix'] = prefix
                        parsed['root'] = remainder
                        parsed['type'] = typ
                        parsed['description'] = desc
                        parsed['normalized'] = remainder
                        break

        # 3. If no rule matches, treat the whole word as the root
        if not parsed['root']:
            parsed['root'] = word_lower
            parsed['normalized'] = word_lower
            parsed['type'] = 'None'
            parsed['description'] = 'No affix found'

        return parsed

    def parse_words(self, words):
        return [self.parse(w) for w in words]

    def display_table(self, results):
        header = (f"{'Word':<10} {'Prefix':<8} {'Root':<10} {'Suffix':<8} "
                  f"{'Type':<15} {'Normalized':<12}")
        print(header)
        print('-' * len(header))
        for r in results:
            print(f"{r['word']:<10} {r['prefix']:<8} {r['root']:<10} {r['suffix']:<8} "
                  f"{r['type']:<15} {r['normalized']:<12}")

def main():
    words = ["unhappy", "happiness", "happily"]
    parser = SentimentMorphParser()
    results = parser.parse_words(words)
    parser.display_table(results)

if __name__ == "__main__":
    main()