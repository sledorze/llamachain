# llamachain
Ollama Langchain Devcontainer

### Install Docker
- Install Docker
- Follow the post installation steps
- Install Docker Compose

### Pull Llama2 LLM
```
git clone git@github.com:rayedbw/llamachain.git
cd llamachain
docker compose run -it -d ollama
docker compose exec -it ollama ollama pull llama2
```

### Setup VSCode
- Open the project in vscdoe `code .`
- Install the `Dev Container` extension pack
- `Ctrl + Shift + P` to open the command palette and type **Rebuild and Reopen in Container**

### Run the application
`python src/main.py` or `F5`

### Try different LLM models
`docker compose run -it -d ollama` to ensure that the container is running

`docker compose exec -it ollama ollama pull gemini` to try the **gemini** model

 


