import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
model = OpenAIModel("gpt-4o-mini", api_key=openai_api_key )
agent = Agent(model=model)   
result = agent.run_sync("What is the capital of India?")
print (result.data)
