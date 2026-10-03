import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# key = os.getenv("GROQ_API_KEY")
# llm = ChatGroq(
#     model="openai/gpt-oss-120b",
#     temperature=0,
#     api_key=key
# )

# ChatGroq can automatically read the API key from your environment variable.
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

# temperature controls how much randomness/variation the AI uses when generating an answer.
# temperature=0 -> Very low randomness. The model tends to give more consistent and predictable answers.
# temperature=0.5 -> Some variation is allowed.
# temperature=1 -> More randomness. The model is more willing to choose different words, structures, and ideas.
# For example:
# Write a story about a robot.
# At 0, you may get a very similar story each time you run it.
# At 0.5, you may get different stories each time, but they will still be somewhat similar.
# At 1, you may get substantially different stories each time.
# | Temperature | Typical use                                                                                   |
# | ----------: | --------------------------------------------------------------------------------------------- |
# |         `0` | Coding, agents, factual tasks                                                                 |
# |       `0.3` | General Q&A                                                                                   |
# |       `0.7` | Creative writing                                                                              |
# |         `1` | Brainstorming / creative content                                                              |
# |         `2` | Very high randomness; generally avoid unless the model specifically supports and calls for it |

question = input("Ask something: ")

response = llm.invoke(question)

print("\nAI:")
print(response.content)
