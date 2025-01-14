import logfire
import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic import BaseModel

class Calculate(BaseModel):
    result: int

load_dotenv()

logfire.configure()

# logfire.info("This is an info message from {name}", name="Ganesan")

model = OpenAIModel("gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY") )    


agent = Agent(model=model, result_type=Calculate)   
result = agent.run_sync("What is 100 + 300?")
logfire.notice("Result: {result}", result=str(result.data))
logfire.info("Result: {result}", result=type(result.data))
logfire.info("Result: {result}", result=result.data.result)
