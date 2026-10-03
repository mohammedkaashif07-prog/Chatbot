import streamlit as st
from main import generate_response

st.title("YOUR AI CHATBOT")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant named Kiyaa. Introduce yourself as Kiyaa.",
        }
    ]

messages_container = st.container(height=650)

user_prompt = st.chat_input(placeholder="Say somehting...")

with messages_container:
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            role_label = "you"
            st.chat_message(name=role_label).write(msg["content"])
        if msg["role"] == "assistant":
            role_label = "bot"
            st.chat_message(name=role_label).write(msg["content"])


if user_prompt:
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    with messages_container:
        st.chat_message(name="You").write(user_prompt)

        with st.spinner("Thinking..."):
            response = generate_response(st.session_state.messages)
            st.chat_message(name="Bot").write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
