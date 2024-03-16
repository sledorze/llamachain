import os

from langchain_community.llms.ollama import Ollama

llama_model = Ollama(model="llama2", base_url=os.environ["OLLAMA_BASE_URL"])

query = "Why is the sky blue?"

for chunk in llama_model.stream(query):
    print(chunk, end="", flush=True)
