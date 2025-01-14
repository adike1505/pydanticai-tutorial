import logfire
import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic import BaseModel, Field
from typing import List
import json

load_dotenv()
logfire.configure()

########### create a pydantic model for the invoice
class ServiceItem(BaseModel):
    description: str = Field(..., description="Description of the service provided")
    quantity: str = Field(..., description="Quantity of the service (e.g., hours, pages, projects)")
    unit_price: float = Field(..., description="Unit price in USD")
    total: float = Field(..., description="Total amount for this service in USD")

class PaymentInstructions(BaseModel):
    bank_name: str = Field(..., description="Name of the bank")
    account_name: str = Field(..., description="Name of the account holder")
    account_number: str = Field(..., description="Bank account number")
    swift_code: str = Field(..., description="SWIFT code for international transfers")

class Invoice(BaseModel):
    invoice_number: str = Field(..., description="Unique identifier for the invoice")
    date_issued: str = Field(..., description="Date when the invoice was issued")
    due_date: str = Field(..., description="Payment due date")
    currency: str = Field(..., description="Currency for the invoice")

    customer_name: str = Field(..., description="Name of the customer")
    company: str = Field(..., description="Name of the customer's company")
    address: str = Field(..., description="Address of the customer")

    services: List[ServiceItem] = Field(..., description="List of services provided")
    subtotal: float = Field(..., description="Subtotal amount in USD")
    tax: float = Field(..., description="Tax amount in USD")
    total_amount_due: float = Field(..., description="Total amount due in USD")

    payment_instructions: PaymentInstructions = Field(..., description="Payment instructions for the invoice")
#############

model = OpenAIModel("gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY") )
# setup the agent to use the model and the Invoice result type
agent = Agent(model=model, result_type=Invoice)

result = agent.run_sync("Please create an invoice for the following services: 1. Web development - 10 hours at $50 per hour 2. Graphic design - 5 hours at $40 per hour 3. Content writing - 3 pages at $20 per page; tax rate is 20%. The payment should be made to the following bank account: Bank Name: Acme Bank Account Name: John Doe Account Number: 1234567890 SWIFT Code: ACMEUS33")
#import ipdb; ipdb.set_trace()
logfire.notice("text prompt llm results: {result}", result=str(result.data))
logfire.info("generated invoice result:: {result}", result=result)
logfire.info("Result type: {result}", result=type(result.data))

with open('data/invoice.md', 'r') as f:
    invoice_data = f.read()

result = agent.run_sync("can you extract the following information from the invoice? the raw data is {invoice_data}")
logfire.notice("invoice data LLM extraction result: {result}", result=str(result.data))
logfire.notice("result type: {result}", result=type(result.data))

