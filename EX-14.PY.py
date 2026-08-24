# Subject-Verb Agreement Checker

singular_subjects = ["boy", "girl", "cat", "dog"]
plural_subjects = ["boys", "girls", "cats", "dogs"]

singular_verbs = ["runs", "plays", "eats", "likes"]
plural_verbs = ["run", "play", "eat", "like"]


def check_agreement(sentence):
    words = sentence.lower().split()

    if len(words) < 2:
        return False

    subject = words[1]
    verb = words[2]

    if subject in singular_subjects and verb in singular_verbs:
        return True

    if subject in plural_subjects and verb in plural_verbs:
        return True

    return False


sentences = [
    "The boy runs",
    "The boys run",
    "The boy run",
    "The girls plays"
]

for sentence in sentences:
    if check_agreement(sentence):
        print(sentence, "-> Accepted")
    else:
        print(sentence, "-> Rejected")