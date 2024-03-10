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
  "type": "function",
  "name": "get_weather",
  "parameters": {
    "city": "Innsbruck",
    "temperature": "23.4",
    "unit": "celsius"
  },
  "execution_info": {
     "timestamp": "192848923",
     "status": "success"
  }
}
```
### Input
Create a Python script that shows the current time.
### Output
write_and_execute_python()
```
{
  "type": "function",
  "name": "write_and_execute_python",
  "parameters": {
    "python_code": "import time\nprint(time)",
    "python_executor": "python3.10"
  },
  "execution_info": {
     "timestamp": "192848923",
     "status": "success",
     "output": "raw_text"
  }
}
```
### Input
How are you doing?
### Output
No Function provided, regular LLM response will be outputted.
```
{
  "type": "response",
  "name": "assistant",
  "parameters": {
    "response": "I'm doing great, thanks. How about you?"
  },
  "execution_info": {
     "timestamp": "192848923",
     "status": "success"
  }
}
```
