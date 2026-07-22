from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Literal
from pydantic import BaseModel, Field

#create the structure
class SupportTicket(BaseModel):  #Defines the structure we expect.
    category: Literal["billing", "technical", "account", "general"] = Field(
        description="The type of problem reported by the customer."
    )

    priority: Literal["low", "medium", "high"] = Field(
        description="How urgently the problem should be handled."
    )

    summary: str = Field(
        description="A short summary of the customer's problem."
    )

    recommended_action: str = Field(
        description="The next action the support team should take."
    )

#load api and model
load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
)
#create a structured version of the model
structured_model = model.with_structured_output( #Creates a version of the model that must return that structure.
    schema=SupportTicket.model_json_schema(), #Converts Python structure into a JSON schema Gemini can follow
    method="json_schema",
)

#customer message example
customer_message = (
    "I cannot access my account the password doesn't work "
    "it gives me an error everytime i try."
)

#invoke the structured model
response = structured_model.invoke(customer_message)

print("Category:", response["category"])
print("Priority:", response["priority"])
print("Summary:", response["summary"])
print("Recommended action:", response["recommended_action"])