# Agent + One Tool

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.tools import tool

load_dotenv()

# LLM
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

# Tool
@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""

    try:
        result = eval(expression)
        return str(result)
    except:
        return "Invalid expression"


# Agent
agent = create_agent(
    model=llm,
    tools=[calculator]
)

# User input
question = input("Ask something: ")


result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": question
        }
    ]
})

print("\nAI:")
print(result["messages"][-1].content)  # -1 means "the last item in the list."


# Sample inputs: 
# What is 2 + 2?
# What is the square root of 16?
# Calculate 5 * 3 - 2.
