from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient

# Connect to your local or deployed MCP Toolbox
toolbox = ToolboxSyncClient("https://toolbox-901927344110.us-central1.run.app/")

# Load the full ApexFlow toolset defined in your YAML
tools = toolbox.load_toolset('apexflow_toolset')

# Define the ApexFlow Logistics Checker Agent
root_agent = Agent(
    name="apexflow_logistics_checker_agent",
    model="gemini-2.5-flash",
    description=(
        "An AI agent that analyzes Formula 1 freight manifests, queries Cloud SQL data, "
        "and detects discrepancies between received shipments and expected inventory. "
        "Designed to support race-week logistics by providing fast, accurate validations."
    ),
    instruction=(
        "You are the ApexFlow Logistics Checker Agent. Your job is to:\n"
        "- Use the provided SQL tools to fetch shipment records and expected inventory.\n"
        "- Compare manifest data with expected F1 parts and quantities.\n"
        "- Identify missing items, mismatched quantities, or delayed shipments.\n"
        "- Produce clear and concise human-readable summaries when responding to the user.\n\n"
        "Only respond to questions related to F1 logistics, manifests, or inventory validation. "
        "If the user asks something outside this domain, politely decline."
    ),
    tools=tools,
)