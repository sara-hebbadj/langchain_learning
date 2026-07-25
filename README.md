# LangChain Learning

This repository contains the small examples I built while learning the basics of LangChain with Python and Gemini.

I kept each concept in a separate file so I could understand what it does before using everything together in a full app.

## What I covered

| File | What I learned |
|---|---|
| `01_basic_model_call.py` | Connect LangChain to Gemini, call the model with `invoke()`, and print the response. |
| `02_prompt_template.py` | Create reusable prompts with variables instead of hardcoding every request. |
| `03_structured_output.py` | Use a Pydantic schema to get predictable fields from the model. |
| `04_tool_calling.py` | Give the model Python tools, execute the tools it requests, and return the results. |
| `05_agent.py` | Use an agent to manage the model and tool-calling loop automatically. |
| `06_chain_composition.py` | Connect a prompt, model, and parser into one fixed chain. |
| `07_memory.py` | Use a checkpointer and thread ID to keep short-term conversation memory. |

## Main ideas I learned

- A **chain** follows fixed steps, for example: `prompt → model → parser`.
- An **agent** can decide which tools it needs and what to do next.
- The model requests a tool, but the Python application or agent executes it.
- Structured output makes the response easier to use in code.
- The same `thread_id` keeps the same conversation history.

## Setup

Install the packages:

```bash
pip install langchain langchain-google-genai langgraph python-dotenv pydantic
```

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

Run any example:

```bash
python 01_basic_model_call.py
```

## Sources

I mainly used the official LangChain documentation and reference:

- [ChatGoogleGenerativeAI integration](https://docs.langchain.com/oss/python/integrations/chat/google_generative_ai)
- [ChatPromptTemplate reference](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate)
- [Tools](https://docs.langchain.com/oss/python/langchain/tools)
- [Agents](https://docs.langchain.com/oss/python/langchain/agents)
- [StrOutputParser reference](https://reference.langchain.com/python/langchain-core/output_parsers/string/StrOutputParser)
- [RunnableSequence reference](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableSequence)
- [Short-term memory](https://docs.langchain.com/oss/python/langchain/short-term-memory)

## Next step

My next step is to use these concepts in a separate LangChain app, then learn LangGraph and RAG separately.
