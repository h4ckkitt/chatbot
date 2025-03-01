import streamlit as st
import requests

st.title("Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

def send_message():
    user_input = st.session_state.user_input
    if user_input:
        # Add user's message to conversation
        st.session_state["messages"].append(("user", user_input))

        # Send request to your FastAPI endpoint
        resp = requests.post(
            "http://localhost:8001/api/v1/chat", 
            json={"message": user_input}
        )
        data = resp.json()

        # Add assistant response
        st.session_state["messages"].append(("assistant", data["response"]))

        # IMPORTANT: Don't do st.session_state["user_input"] = ""
        # st.chat_input will auto-clear after submission.

# Display conversation
for role, text in st.session_state["messages"]:
    with st.chat_message(role):
        st.write(text)

# Provide a chat-style input
st.chat_input("Type your message...", key="user_input", on_submit=send_message)