# 🚧 Work in Progress
🚧 This repository is considered work-in-progress and useless, until this notification is removed. :)

## What is it?
**Open Functions extends off-the-shelf Language Large Models (LLMs) like Mistral and Llama with function-calling capabilities.** It helps transitioning your LLM into a dynamic, interactive AI powerhouse by enabling seamless and reliable structured JSON outputs.

## 🌟 Features
- **Function Calling for all LLMs**: Empower your LLMs to execute and call functions.
- **Build interactive LLM experiences**: Transform passive models into active assistants, enabling data analysis, code execution and content generation for open models.

## Install
1. Clone this repository: `git clone https://github.com/localmind-ai/open-functions`
2. Install Dependencies: `pip install -r requirements.txt`
1. Run the app: `python3 open-functions.py`

## How it works
You define the structure of your function in an instruction prompt. Open Functions will try to follow your instructions and make sure that the output is always valid and well-structured JSON. 
## Examples
### Input
It's 23.4 C Degrees in Innsbruck.
### Output
get_weather()
```
{
  "city": "Innsbruck",
  "temperature": "23.4",
  "unit": "celsius",
  "function_call": "get_weather",
  "timestamp": "192848923"
}
```
### Input
Create a Python script that shows the current time.
### Output
write_and_execute_python()
```
{
  "python_code": "import time\n print(time)",
  "python_executor": "python3.10",
  "python_output": "raw_text",
  "function_call": "write_and_execute_python",
  "timestamp": "192848923"
}
```
### Input
How are you doing?
### Output
No Function provided, regular LLM response will be outputted.
```
{
  "response": "I'm doing great, thanks. How about you?",
  "function_call": "none",
  "timestamp": "192848923"
}
```
