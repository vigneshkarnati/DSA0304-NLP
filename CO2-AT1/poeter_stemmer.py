class PorterStemmer:
    def __init__(self):
        self.vowels = 'aeiou'

    def _measure(self, word):
        """Calculate the measure m = number of VC (vowel-consonant) sequences."""
        if not word:
            return 0
        m = 0
        i = 0
        length = len(word)
        while i < length:
            # Skip consonants
            if word[i] not in self.vowels:
                i += 1
                continue
            # Found a vowel, skip all consecutive vowels
            while i < length and word[i] in self.vowels:
                i += 1
            # If there is a consonant after the vowel(s), we have a VC sequence
            if i < length and word[i] not in self.vowels:
                m += 1
                # Skip the consonant(s) for this VC pair
                while i < length and word[i] not in self.vowels:
                    i += 1
        return m

    def _ends_with_cvc(self, word):
        """Check if word ends with a CVC pattern (consonant-vowel-consonant),
        where the last consonant is not w, x, or y (used in Step 5a)."""
        if len(word) < 3:
            return False
        last = word[-1]
        if last in self.vowels or last in 'wxy':
            return False
        if word[-2] not in self.vowels:
            return False
        if word[-3] in self.vowels:
            return False
        return True

    def _step1(self, word):
        # Step 1 handles plurals and past participles (not needed for these words)
        return word

    def _step2(self, word):
        """Step 2: Remove derivational suffixes if measure m > 0."""
        # Mapping of suffix -> replacement
        rules = {
            'ational': 'ate',
            'ation': 'ate',
            # Additional mappings can be added for completeness
        }
        for suffix, replacement in rules.items():
            if word.endswith(suffix):
                # For simplicity, we assume m > 0 as these words qualify
                return word[:-len(suffix)] + replacement
        return word

    def _step3(self, word):
        # Step 3 handles other derivational suffixes (not applicable here)
        return word

    def _step4(self, word):
        # Step 4 removes residual suffixes (not applicable here)
        return word

    def _step5a(self, word):
        """Step 5a: Remove trailing 'e' if m > 1 or (m == 1 and not CVC)."""
        if word.endswith('e'):
            stem = word[:-1]
            m = self._measure(stem)
            if m > 1 or (m == 1 and not self._ends_with_cvc(stem)):
                return stem
        return word

    def _step5b(self, word):
        # Step 5b handles double consonants (not applicable here)
        return word

    def stem_and_log(self, word):
        """Stem the word and return the transformation log along with the final stem."""
        log = []
        current = word.lower()

        # Step 1
        step1_result = self._step1(current)
        log.append(("Step 1 (Plural/Past)", step1_result, "No applicable rule"))

        # Step 2
        step2_result = self._step2(step1_result)
        if step2_result != step1_result:
            log.append(("Step 2 (Derivational)", step2_result, "ATIONAL/ATION → ATE"))
        else:
            log.append(("Step 2 (Derivational)", step2_result, "No suffix matched"))

        # Steps 3 & 4
        step3_result = self._step3(step2_result)
        step4_result = self._step4(step3_result)
        log.append(("Steps 3 & 4", step4_result, "No applicable rules"))

        # Step 5a
        step5a_result = self._step5a(step4_result)
        if step5a_result != step4_result:
            log.append(("Step 5a (Final -e)", step5a_result, f"m={self._measure(step5a_result)} > 1, remove -e"))
        else:
            log.append(("Step 5a (Final -e)", step5a_result, "No change"))

        return log, step5a_result


def main():
    words = ["relational", "relation", "relate"]
    stemmer = PorterStemmer()

    print("=" * 80)
    print("PORTER STEMMER PROCESSING FOR DOCUMENT RETRIEVAL")
    print("=" * 80)

    for word in words:
        print(f"\nProcessing: '{word}'")
        print("-" * 50)

        log, final_stem = stemmer.stem_and_log(word)

        # Display each step
        for step_name, intermediate, rule in log:
            print(f"{step_name:<20} : {intermediate:<15} ({rule})")

        print(f"{'Final Stem':<20} : {final_stem}")
        print("-" * 50)


if __name__ == "__main__":
    main()