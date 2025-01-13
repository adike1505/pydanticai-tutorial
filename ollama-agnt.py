from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from colorama import Fore


ollama_model = OllamaModel(model_name='mistral')
agent = Agent(model=ollama_model)

result = agent.run_sync("What is the capital of Karnataka state? and tell me a joke from that city")
print (Fore.GREEN + result.data)
