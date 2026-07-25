from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
)

memory = InMemorySaver()

agent = create_agent(
    model = model ,
    tools = [] ,
    system_prompt=(
        "You are a helpful assistant. "
        "Remember information the user shares earlier in the conversation."
    ),
    checkpointer = memory
    
)
config = {
    "configurable": {
        "thread_id": "conversation-1",
    }
}
first_result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "My name is Sara and I am learning LangChain.",
            }
        ]
    },
    config,
)

print("First response:")
print(first_result["messages"][-1].text)

second_result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is my name and what am I learning?",
            }
        ]
    },
    config,
)

print("\nSecond response:")
print(second_result["messages"][-1].text)