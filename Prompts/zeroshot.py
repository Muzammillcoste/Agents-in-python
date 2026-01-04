from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# Zero-shot prompt
client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {   "role": "system",
            "content": "You are a helpful Math Assistant. Which answer questions related to math. and say sorry if question is not related to math."
        },
        {
            "role": "user",
            "content": "Explain to me how AI works"
        }
    ]
)

print(response.choices[0].message.content)
