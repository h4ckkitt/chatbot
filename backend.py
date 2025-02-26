from fastapi import FastAPI
from pydantic import BaseModel
from langchain_ollama import ChatOllama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

app = FastAPI()

# 1) Create the LLM (Ollama)
#    By default, it may connect to the local Ollama server on http://localhost:11411
#    Adjust parameters as needed for your environment.
llm = ChatOllama(
    base_url="http://localhost:11434",  # typical default for Ollama
    model="llama3.1:8b",                  # example model name
)

# 2) Build a conversation chain with memory
conversation = ConversationChain(
    llm=llm,
    memory=ConversationBufferMemory(),
)

# Pydantic model for incoming chat requests
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    """
    Receives a user message and returns an AI-generated response.
    """
    # Pass the user message to the chain
    response = conversation.run(req.message)
    return {"response": response}