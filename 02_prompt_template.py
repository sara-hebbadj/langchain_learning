from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
)
prompt = ChatPromptTemplate(
    [("system", " you are a patient teacher who explains technical concepts simply"),
     ("user", " explain {topic} to a {audience} in three short bullet points"),
    ]
)

formatted_prompt = prompt.invoke(
    {"topic":"ai agents",
     "audience" : "beginner python developper"}
)

response = model.invoke(formatted_prompt)

print(response.text)