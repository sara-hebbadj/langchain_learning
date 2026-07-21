from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
)
response = model.invoke("say hello in one short sentence")
print (response.text)

## implement first LangChain Gemini model invocation
## Load an API key.
## Connect LangChain to Gemini.
## Call the model with invoke().
## Print the response.
