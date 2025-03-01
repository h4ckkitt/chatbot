from fastapi import FastAPI
from pydantic import BaseModel
from langchain_ollama import ChatOllama
from langchain.schema import HumanMessage

app = FastAPI()

# Create an Ollama LLM instance
# 'model' should match whatever you've pulled via `ollama pull <model>`
ollama_llm = ChatOllama(
    model="llama3.1:8b",
    verbose=True,
    temperature=0.2,
)

class ChatRequest(BaseModel):
    message: str

@app.post("/api/v1/chat")
async def chat_endpoint(req: ChatRequest):
    """
    Receives a user message and returns an AI-generated response from Ollama.
    """
    # Build a single HumanMessage for the user's input
    user_message = HumanMessage(content=req.message)

    # For a single-turn approach, just pass a list with one HumanMessage
    ai_response = ollama_llm.invoke([user_message])

    # ai_response is an AIMessage object with a .content attribute
    return {"response": ai_response.content}