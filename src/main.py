import os

from langchain_community.chat_models.ollama import ChatOllama 

llama_model = ChatOllama(model="llama2", base_url=os.environ["OLLAMA_BASE_URL"])

query = "Why is the sky blue?"

for chunk in llama_model.stream(query):
    print(chunk.content, end="", flush=True)
