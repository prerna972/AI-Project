# Agent + Multiple Tools

# pip install wikipedia

import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.tools import tool
import wikipedia

load_dotenv()

# -------------------------
# LLM
# -------------------------

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)


# -------------------------
# Calculator Tool
# -------------------------

@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""

    try:
        return str(eval(expression))
    except:
        return "Invalid expression"


# -------------------------
# Wikipedia Tool
# -------------------------

@tool
def wikipedia_search(query: str) -> str:
    """Search Wikipedia for information."""

    try:
        return wikipedia.summary(query, sentences=3)
    except Exception:
        return "No information found."


# -------------------------
# Agent
# -------------------------

agent = create_agent(
    model=llm,
    tools=[
        calculator,
        wikipedia_search
    ]
)


# -------------------------
# User
# -------------------------

question = input("Ask something: ")

result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": question
        }
    ]
})


# -------------------------
# Output
# -------------------------

print("\nAI:")
print(result["messages"][-1].content)


# Sample inputs: 
# What is 500 * 25?
# What is the capital of France?
# Who is Albert Einstein?
