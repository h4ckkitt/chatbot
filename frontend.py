import streamlit as st
import requests

st.title("LangChain + Ollama Chat Demo")

# Keep chat messages in session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

def handle_input():
    user_input = st.session_state.user_input
    if user_input:
        # Send the user message to the backend
        resp = requests.post(
            "http://localhost:8000/chat",
            json={"message": user_input},
            timeout=60
        )
        data = resp.json()

        # Store messages in session
        st.session_state["messages"].append(("You", user_input))
        st.session_state["messages"].append(("AI", data["response"]))

        # Clear the text input
        st.session_state.user_input = ""

# A text_input with on_change triggers handle_input when user presses Enter
st.text_input("Enter your message:", key="user_input", on_change=handle_input)

# Display the chat
for speaker, text in st.session_state["messages"]:
    st.write(f"**{speaker}:** {text}")