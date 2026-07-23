from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a professional customer-support assistant.",
        ),
        (
            "user",
            """
Write a concise and helpful response to this customer message.

Customer message:
{customer_message}

Tone:
{tone}
""",
        ),
    ]
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke(
    {
        "customer_message": (
            "i was charged twice for my order and i need a refund"
        ),
        "tone": "apologetic and reassuring",
    }
)

print(result)