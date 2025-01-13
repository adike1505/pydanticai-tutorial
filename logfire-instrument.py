import logfire
import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

load_dotenv()

logfire.configure()

logfire.info("This is an info message from {name}", name="Ganesan")

model = OpenAIModel("gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY") )    
agent = Agent(model=model)

@logfire.instrument("apply multiplication to {x=} and {y=}")
def multiply(x, y):
    return x * y

with logfire.span("calling openai gpt-40-mini ") as span:
    try:
        result = agent.run_sync(f"can u confirm that {multiply(200, 3)} is the result of 200 * 3 ? also include answer")
        span.set_attribute("result", result.data)
        logfire.info("info Result: {result}", result=result.data)
        #raise ValueError(result.data)
    except ValueError as e:
        span.record_exception(e)
