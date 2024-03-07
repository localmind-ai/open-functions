# OpenFunctions
OpenFunctions gives open LLMs like Mistral & Llama advanced function calling capabilities.
Use LLMs as interactive tools that do tasks for you. Whether you're looking to streamline complex data analysis, automate content generation, or develop innovative AI-driven solutions, OpenFunctions provides the key to unlocking new levels of AI agent performance and productivity.
## How it works
You can create any function structure you want. For example:
```
{
  "temperature": "23.4",
  "unit": "celsius",
  "timestamp": "192848923"
}
```
or
```
{
  "python_code": "import time\n print(time)",
  "python_executor": "python3.10",
  "python_output": "json", "text"
}
```
