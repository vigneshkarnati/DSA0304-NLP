# Top-Down Parser

grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["sees"], ["likes"]]
}

sentence = "the cat sees the dog".split()


def parse(symbol, position):
    if symbol not in grammar:
        if position < len(sentence) and sentence[position] == symbol:
            return position + 1
        return None

    for production in grammar[symbol]:
        current = position
        success = True

        for item in production:
            current = parse(item, current)

            if current is None:
                success = False
                break

        if success:
            return current

    return None


result = parse("S", 0)

if result == len(sentence):
    print("Sentence accepted")
else:
    print("Sentence rejected")