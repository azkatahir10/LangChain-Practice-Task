# 🧠 LangChain Tool Calling Exercise Report

## 📌 Objective

Build an intelligent assistant using **LangChain** that can access external tools to respond to queries requiring real-time information. Specifically, create a tool that retrieves the **current date and time**, integrate it into an **LLM agent**, and demonstrate tool calling capabilities.

---

## ⚙️ Tools & Libraries Used

* **LangChain**
* **Google Generative AI (Gemini)**
* **Python 3.10+**
* **Datetime module** (for time retrieval)

---

## 🧰 Custom Tool: `get_current_datetime`

### ✅ Purpose:

Return the current date and time in a readable format.

### 🧾 Definition:

```python
from datetime import datetime
from langchain.tools import tool

@tool
def get_current_datetime() -> str:
    """Returns the current date and time."""
    return datetime.now().strftime("%A, %B %d, %Y %I:%M:%S %p")
```

---

## 🧠 LLM Agent Setup

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableConfig

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=os.getenv("GOOGLE_API_KEY"))
tool_bound_llm = llm.bind_tools([get_current_datetime])
```

---

## 🤖 Tool Invocation Logic

```python
response = tool_bound_llm.invoke("What is the current time and date?")

if response.tool_calls:
    for tool_call in response.tool_calls:
        if tool_call["name"] == "get_current_datetime":
            result = get_current_datetime.invoke(tool_call["args"])
            print("\n\U0001F4C5 Tool Output:", result)
```

---

## 🧪 Example Execution

### 🗣 Prompt:

```
What is the current time and date?
```

### 🧠 LLM Response:

```
"I need to use the get_current_datetime tool to answer that."
```

### 🔧 Tool Call:

```
Tool Name: get_current_datetime
Tool Arguments: {}
```

### 📅 Final Output:

```
Monday, July 31, 2025 06:45:10 PM
```

---

## ✅ Assignment Requirements Checklist

| Requirement                    | Status |
| ------------------------------ | ------ |
| Custom Tool using `@tool`      | ✅      |
| Bind tool to an LLM agent      | ✅      |
| Trigger tool call from prompt  | ✅      |
| Execute tool dynamically       | ✅      |
| Display final response to user | ✅      |

---

## 📦 Suggested Project Structure

```
langchain_tool_agent/
├── tool_agent_app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧾 Notes

* LLM tool calls are now handled via `.invoke()` due to deprecation of `__call__()` in LangChain Core ≥ 0.1.47.
* Tool outputs are printed in structured format with emoji labels.

---

## 🧑‍💻 Author

Azka Tahir
LangChain Tool Agent — 2025
