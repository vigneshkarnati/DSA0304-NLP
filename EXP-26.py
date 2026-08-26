from transformers import pipeline

# Load English to French translation model
translator = pipeline(
    "translation_en_to_fr",
    model="Helsinki-NLP/opus-mt-en-fr"
)

text = "I love learning Natural Language Processing."

result = translator(text)

print("English:")
print(text)

print("\nFrench:")
print(result[0]["translation_text"])