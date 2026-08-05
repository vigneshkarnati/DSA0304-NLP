class FiniteStateMorphParser:
    def __init__(self):
        # Irregular forms: direct mapping to root
        self.irregular = {
            'written': 'write'
        }

        # Regular suffix rules: (suffix, transformation_function)
        # transformation takes the stem (word without suffix) and returns the root
        self.suffix_rules = [
            ('s', lambda stem: stem),                # writes -> write
            ('ing', lambda stem: stem + 'e' if stem == 'writ' else stem)   # writing -> write
        ]
        # Sort by suffix length descending to match longer suffixes first
        self.suffix_rules.sort(key=lambda x: len(x[0]), reverse=True)

    def parse(self, word):
        word_lower = word.lower()
        result = {
            'word': word,
            'root': '',
            'suffix': '',
            'type': '',
            'transition_path': [],
            'breakdown': '',
            'normalized': ''
        }

        # 1. Check for irregular
        if word_lower in self.irregular:
            result['root'] = self.irregular[word_lower]
            result['suffix'] = '(irregular)'
            result['type'] = 'Irregular'
            result['normalized'] = result['root']
            result['breakdown'] = f"{result['root']} (irregular)"
            result['transition_path'] = ['START', 'IRREGULAR_LOOKUP', 'ACCEPT']
            return result

        # 2. Try regular suffix rules (longest first)
        for suffix, transform in self.suffix_rules:
            if word_lower.endswith(suffix):
                stem = word_lower[:-len(suffix)]
                if stem:  # ensure non‑empty stem
                    result['suffix'] = suffix
                    result['root'] = transform(stem)
                    result['type'] = 'Regular'
                    result['normalized'] = result['root']
                    # Build breakdown string
                    if suffix == 'ing' and stem == 'writ':
                        result['breakdown'] = "write (drop 'e') + ing"
                    else:
                        result['breakdown'] = f"{result['root']} + {suffix}"
                    # Simulate state transitions
                    result['transition_path'] = self._trace_transitions(word_lower, stem, suffix)
                    return result

        # 3. Fallback: no rule matched
        result['root'] = word_lower
        result['suffix'] = ''
        result['type'] = 'None'
        result['normalized'] = word_lower
        result['breakdown'] = 'No suffix found'
        result['transition_path'] = ['START', 'READING', 'ACCEPT']
        return result

    def _trace_transitions(self, word, stem, suffix):
        """Simulate a finite‑state path for the given word."""
        path = ['START']
        # Stem part: READING state
        for _ in stem:
            path.append('READING')
        # Suffix part: SUFFIX state
        for _ in suffix:
            path.append('SUFFIX')
        # Apply transformation: TRANSFORM
        path.append('TRANSFORM')
        path.append('ACCEPT')
        return path

    def parse_words(self, words):
        return [self.parse(w) for w in words]

    def display_table(self, results):
        headers = ['Word', 'Root', 'Suffix', 'Type', 'Transition Path', 'Breakdown', 'Normalized']
        col_widths = [10, 10, 12, 10, 30, 25, 12]
        # Print header
        header_line = '  '.join(f'{h:<{w}}' for h, w in zip(headers, col_widths))
        print(header_line)
        print('-' * len(header_line))

        for r in results:
            # Format transition path as a string
            trans_str = ' → '.join(r['transition_path'])
            row = [
                r['word'],
                r['root'],
                r['suffix'],
                r['type'],
                trans_str,
                r['breakdown'],
                r['normalized']
            ]
            line = '  '.join(f'{str(val):<{w}}' for val, w in zip(row, col_widths))
            print(line)


def main():
    words = ["writes", "writing", "written"]
    parser = FiniteStateMorphParser()
    results = parser.parse_words(words)
    parser.display_table(results)


if __name__ == "__main__":
    main()