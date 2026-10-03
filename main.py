
import os

from dotenv import load_dotenv
from pydantic import BaseModel

from langchain_groq import ChatGroq
from langchain.agents import create_agent

from tools import search_tool, wiki_tool, save_tool


# Load environment variables
load_dotenv()


# Response structure
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


# Groq configuration
key = os.getenv("GROQ_API_KEY")

MODEL = "openai/gpt-oss-120b"


# Create ChatGroq LLM
llm = ChatGroq(
    model=MODEL,
    temperature=0,
    api_key=key
)


# Tools
tools = [
    search_tool,
    wiki_tool,
    save_tool
]


# Create agent
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
    You are a research assistant that will help generate a research paper.

    Answer the user's query and use the necessary tools.

    Provide:
    - topic
    - summary
    - sources
    - tools_used

    Return a clear and useful research response.
    """
)


# User query
query = input("What can I help you research? ")


# Run agent
result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": query
            }
        ]
    }
)


# Display final response
print("\n--- Research Result ---\n")

messages = result.get("messages", [])

if messages:
    final_message = messages[-1]

    print(final_message.content)
else:
    print(result)
