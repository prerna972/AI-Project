
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

from datetime import datetime
import requests


# ---------------------------------------------------------
# Save research to text file
# ---------------------------------------------------------

@tool
def save_tool(data: str, filename: str = "research_output.txt") -> str:
    """
    Saves research data to a text file.
    """

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    formatted_text = (
        "--- Research Output ---\n"
        f"Timestamp: {timestamp}\n\n"
        f"{data}\n\n"
    )

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"


# ---------------------------------------------------------
# DuckDuckGo Search
# ---------------------------------------------------------

search = DuckDuckGoSearchRun()


@tool
def search_tool(query: str) -> str:
    """
    Search the web for information.
    """

    return search.invoke(query)


# ---------------------------------------------------------
# Wikipedia Search
# ---------------------------------------------------------

@tool
def wiki_tool(query: str) -> str:
    """
    Search Wikipedia for information.
    """

    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "utf8": 1,
        "srlimit": 3
    }

    headers = {
        "User-Agent": "ResearchAgent/1.0"
    }

    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    results = data.get("query", {}).get("search", [])

    if not results:
        return f"No Wikipedia results found for: {query}"

    output = []

    for result in results:
        title = result.get("title", "")
        snippet = result.get("snippet", "")

        output.append(
            f"Title: {title}\n"
            f"Information: {snippet}"
        )

    return "\n\n".join(output)
