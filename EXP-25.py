from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

prompt = "Write a short paragraph about Natural Language Processing."

response = client.responses.create(
    model="gpt-5-mini",
    input=prompt
)

print("Generated Text:")
print(response.output_text)