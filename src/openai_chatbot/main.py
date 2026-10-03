import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def generate_response(messages):
    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        raise ValueError("Missing api key in .env")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1", api_key=os.getenv("OPENROUTER_API_KEY")
    )

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0.7,
    )

    return response.choices[0].message.content
