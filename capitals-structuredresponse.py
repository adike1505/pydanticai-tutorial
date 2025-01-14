import logfire
import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic import BaseModel

load_dotenv()
logfire.configure()

class Capital(BaseModel):
    name: str
    year_founded: int
    short_description: str

oai_model = OpenAIModel("gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
agent = Agent(model=oai_model, result_type=Capital)
result = agent.run_sync("what is the capital of China?")
logfire.notice("capital Result: {result}", result=result.data)
