import os

from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st
from streamlit.errors import StreamlitSecretNotFoundError

load_dotenv()


def generate_response(messages):
    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        try:
            api_key = st.secrets["OPENROUTER_API_KEY"]
        except (KeyError, StreamlitSecretNotFoundError):
            api_key = None

    if not api_key:
        raise ValueError(
            "Missing OPENROUTER_API_KEY. Add it to Streamlit Cloud secrets or your local .env file."
        )

    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0.7,
    )

    return response.choices[0].message.content
