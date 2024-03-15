from ollama import Client

client = Client(host="http://ollama:11434")

stream = client.chat(
    model="llama2",
    messages=[{"role": "user", "content": "Why is the sky blue?"}],
    stream=True,
)

for chunk in stream:
    print(chunk["message"]["content"], end="", flush=True)
