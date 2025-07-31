import os
from datetime import datetime
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool

# Load environment variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

# Define the custom tool
@tool
def get_current_datetime() -> str:
    """Returns the current date and time in a readable format."""
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

# Create the LLM
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",  # or models/gemini-1.5-pro
    google_api_key=google_api_key,
    temperature=0
)

# Bind tools
tools = [get_current_datetime]
llm_with_tools = llm.bind_tools(tools)

# User prompt
user_query = "What is the current time and date?"

# Invoke the LLM
response = llm_with_tools.invoke(user_query)

# Output LLM response
print("\n📩 LLM Response:\n")
print(response.content)

# Check if any tools were called
if hasattr(response, "tool_calls") and response.tool_calls:
    print("\n🔧 Tool Calls Detected:\n")
    for tool_call in response.tool_calls:
        print(f"Tool Name: {tool_call['name']}")
        print(f"Tool Arguments: {tool_call['args']}")

        # Call the tool properly using invoke
        for tool in tools:
            if tool.name == tool_call['name']:
                result = tool.invoke(tool_call['args'])  # ✅ correct way
                print(f"\n✅ Tool Result:\n{result}")
else:
    print("\nℹ️ No tool call was made.\n")
