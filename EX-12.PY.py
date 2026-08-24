# Simple Earley Parser

grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["sees"], ["likes"]]
}

sentence = "the cat sees the dog".split()


def earley_parser(sentence):
    n = len(sentence)

    # Each state is:
    # (lhs, rhs, dot, start_position)

    chart = [set() for _ in range(n + 1)]

    chart[0].add(("S'", ("S",), 0, 0))

    for i in range(n + 1):
        changed = True

        while changed:
            changed = False

            for lhs, rhs, dot, start in list(chart[i]):

                # Prediction
                if dot < len(rhs):
                    symbol = rhs[dot]

                    if symbol in grammar:
                        for production in grammar[symbol]:
                            state = (symbol, tuple(production), 0, i)

                            if state not in chart[i]:
                                chart[i].add(state)
                                changed = True

                # Completion
                else:
                    for l, r, d, s in list(chart[start]):
                        if d < len(r) and r[d] == lhs:
                            state = (l, r, d + 1, s)

                            if state not in chart[i]:
                                chart[i].add(state)
                                changed = True

        # Scanning
        if i < n:
            for lhs, rhs, dot, start in list(chart[i]):
                if dot < len(rhs):
                    symbol = rhs[dot]

                    if symbol not in grammar and symbol == sentence[i]:
                        chart[i + 1].add(
                            (lhs, rhs, dot + 1, start)
                        )

    final_state = ("S'", ("S",), 1, 0)

    return final_state in chart[n]


if earley_parser(sentence):
    print("Sentence accepted")
else:
    print("Sentence rejected")