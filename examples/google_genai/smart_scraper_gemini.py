
import os
from dotenv import load_dotenv
from scrapegraphai.utils import prettify_exec_info
from scrapegraphai.graphs import SmartScraperGraph
load_dotenv()


# ************************************************
# Define the configuration for the graph
# ************************************************

gemini_key = os.getenv("GOOGLE_APIKEY")

graph_config = {
    "llm": {
        "api_key": gemini_key,
        "model": "google_genai/gemini-1.5-flash-latest",
        "convert_system_message_to_human":"True"
    },
}

# ************************************************
# Create the SmartScraperGraph instance and run it
# ************************************************

smart_scraper_graph = SmartScraperGraph(
    prompt="List the title of the first articles from Wired",
    # also accepts a string with the already downloaded HTML code
    source="https://www.wired.com",
    config=graph_config,
    system = "translate all answers or results or titles into the swedish language"
)

result = smart_scraper_graph.run()
print(result)


