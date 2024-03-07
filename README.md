# OpenFunctions
OpenFunctions gives open LLMs like Mistral & Llama advanced function calling capabilities.
Use LLMs as interactive tools that do tasks for you. Whether you're looking to streamline complex data analysis, automate content generation, or develop innovative AI-driven solutions, OpenFunctions provides the key to unlocking new levels of AI agent performance and productivity.
## How it works
You can define any function structure. OpenFunctions will follow it and make sure the LLM always outputs the correct output and structure. 
## Examples
### Input
It's 23.4 C Degrees in Innsbruck.
### Output
*get_weather()*
```
{
  "city": "Innsbruck",
  "temperature": "23.4",
  "unit": "celsius",
  "timestamp": "192848923"
}
```
### Input
Create a Python script that shows the current time.
```
{
  "python_code": "import time\n print(time)",
  "python_executor": "python3.10",
  "python_output": "json", "text"
}
```
### Output
