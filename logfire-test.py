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

#note - types of logfire logs are notice, debug, info, warn, error, fatal
with logfire.span("calling openai gpt-40-mini ") as span:
    try:
        result = agent.run_sync("What is the capital of India?")
        span.set_attribute("result", result.data)
        #logfire.notice("notice Result: {result}", result=result.data)
        logfire.info("info Result: {result}", result=result.data)
        # logfire.warn("warn Result: {result}", result=result.data)
        # logfire.debug("debug Result: {result}", result=result.data)
        # logfire.error("error Result: {result}", result=result.data)
        # logfire.fatal("fatal Result: {result}", result=result.data)
        raise ValueError(result.data)
    except ValueError as e:
        span.record_exception(e)
    