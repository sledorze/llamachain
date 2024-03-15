import os
from ollama import Client

client = Client(host=os.environ["OLLAMA_BASE_URL"])

stream = client.chat(
    model="llama2",
    messages=[{"role": "user", "content": "Why is the sky blue?"}],
    stream=True,
)

for chunk in stream:
    print(chunk["message"]["content"], end="", flush=True)
