# llamachain
Ollama Langchain Devcontainer

### Install Docker
- Install [Docker](https://docs.docker.com/engine/install/)
- Follow the post installation steps
- Install [Docker Compose](https://docs.docker.com/compose/install/)

### Download project
```bash
git clone git@github.com:rayedbw/llamachain.git
cd llamachain
```

### Setup vscode
- Open the project in vscode `code .`
- Install the `Dev Container` extension pack
- `Ctrl + Shift + P` to open the command palette and type **Rebuild and Reopen in Container**

### Pull Llama2 model
In a terminal window outside of the container run the following to download the llama2 model in your container:
```bash
docker exec llamachain-ollama-1 ollama pull llama2
```

### Run the application in vscode
`python src/main.py` or press `F5`

### Try different LLM models
`docker exec llamachain-ollama-1 ollama pull gemma` to try the **gemma** model

Don't forget to actually use the model in your code by changing the `model` parameter.
```python
from langchain_community.chat_models.ollama import ChatOllama

llm = ChatOllama(model="gemma", base_url=os.environ["OLLAMA_BASE_URL"])
```

### To use OpenAI
- Create an api key from the [OpenAI website](https://platform.openai.com/api-keys)
- Create a `.env` file at the project root
- Add `OPENAI_API_KEY=<your_api_key>`

 


