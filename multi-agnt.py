from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.models.ollama import OllamaModel
from colorama import Fore
import os
from dotenv import load_dotenv

load_dotenv()
open_aimodel = OpenAIModel("gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
ollama_model = OllamaModel(model_name='mistral')

openai_agent = Agent(model=open_aimodel)
result = openai_agent.run_sync("What is the capital of India?")
print (Fore.GREEN, "OpenAI Agent - ", result.data)

# capture last message
msg_history = result.new_messages()

ollama_agent = Agent(model=ollama_model)
result = ollama_agent.run_sync("tell me about the history of the city?", message_history=msg_history)
print (Fore.RED, "Ollama Agent - ", result.data)

