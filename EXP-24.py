dialog = [
    "Hello, how are you?",
    "I am fine.",
    "Can you help me with my assignment?",
    "Sure, I can help you.",
    "Thank you.",
    "Goodbye."
]

def dialog_act(sentence):
    text = sentence.lower()

    if any(word in text for word in ["hello", "hi", "hey"]):
        return "Greeting"

    elif "?" in sentence:
        return "Question"

    elif any(word in text for word in ["thank", "thanks"]):
        return "Thanking"

    elif any(word in text for word in ["goodbye", "bye"]):
        return "Goodbye"

    elif any(word in text for word in ["can you", "please", "could you"]):
        return "Request"

    else:
        return "Statement/Answer"


print("Dialog Act Recognition:\n")

for sentence in dialog:
    print(sentence, "->", dialog_act(sentence))