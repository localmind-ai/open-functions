# 🚧 Work in Progress
🚧 This repository is considered work-in-progress and useless, until this notification is removed. :)

## What is it?
**Open Functions extends off-the-shelf Language Large Models (LLMs) like Mistral and Llama with function-calling capabilities.** It helps transitioning your LLM into a dynamic, interactive AI assistant by enabling seamless and reliable structured JSON outputs. Use these outputs to call functions, scripts and programs.

## 🌟 Features
- **Function Calling for all LLMs**: Empower your LLMs to execute and call functions.
- **Build interactive LLM experiences**: Transform passive models into active assistants, enabling task execution capabilities to open models.

## Install
1. Clone this repository: `git clone https://github.com/localmind-ai/open-functions`
2. Install Dependencies: `pip install -r requirements.txt`
3. Run the API: `uvicorn open-functions:app --reload`
4. Call your API:
```
curl -X POST http://127.0.0.1:8000/function_call \
-H "Content-Type: application/json" \
-d '{
    "text": "The weather in innsbruck is beatuiful, 20°C and sunny."
}'
```
### Response
```
{
    "type": "function",
    "name": "get_weather",
    "parameters": {
        "city": "Innsbruck",
        "temperature": "20",
        "conditions": "sunny"
    },
    "status": "success",
    "timestamp": "2024-03-10T02:53:13.685618"
}
```
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
