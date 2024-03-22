import os

from langchain_community.llms.ollama import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

OLLAMA_BASE_URL = os.environ["OLLAMA_BASE_URL"]

model = Ollama(model="mistral", base_url=OLLAMA_BASE_URL)
prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")
parser = StrOutputParser()

chain = prompt | model | parser

for chunk in chain.stream({"topic": "Harrison Ford"}):
    print(chunk, end="", flush=True)
