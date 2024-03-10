# 🚧 Work in Progress
🚧 This repository is considered work-in-progress and useless, until this notification is removed. :)

# Open Functions
**Extend LLMs like Mistral and Llama with advanced function calling capabilities.**

Open Functions transforms a regular LLM that was not pre-trained for function calling and extends it with function calling capabilities. these models to call and execute functions, Open Functions transforms LLMs into powerful, interactive tools capable of completing complex tasks and generating structured outputs. Whether you're aiming to streamline data analysis, automate content creation, or develop innovative AI-driven solutions, Open Functions provide the key to unlocking the full potential of open-source LLMs, ensuring reliable performance.

## Install
After cloning this repository, run `python3 open-functions.py`.

## How it works
You define the structure of your function in an instruction prompt. Open Functions will try to follow your instructions and make sure that the output is always valid JSON with your defined structure. 
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
