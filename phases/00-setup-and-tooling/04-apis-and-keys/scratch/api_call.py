import os
from google import genai

key = os.getenv("GEMINI_API_KEY")

if not key:
    raise ValueError("GEMINI_API_KEY belum diatur!")

client = genai.Client(api_key=key)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="What is a neural network in one sentence?",
)

print(interaction.output_text)